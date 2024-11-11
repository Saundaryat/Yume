import json
from langchain_google_vertexai import ChatVertexAI
from langchain.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import PydanticOutputParser
from models import NutritionalInfo, HealthRecommendation, NutritionFacts
from langchain_google_vertexai import VertexAI
from langchain.schema import AIMessage, HumanMessage
from vertexai.vision_models import ImageTextModel
from google.oauth2 import service_account
from google.auth import default
from google_setup import initialize_google
import numpy as np
import io
import os
import yaml
import PIL
import warnings
import logging

import hashlib
from cachetools import cached, TTLCache

from langsmith import traceable
from vertexai.preview.generative_models import GenerativeModel, Image

# Suppress specific warnings
warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>")

# Suppress TensorFlow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
logging.getLogger('tensorflow').setLevel(logging.FATAL)

# Suppress other logging
logging.getLogger('absl').setLevel(logging.ERROR)
logging.getLogger('grpc').setLevel(logging.ERROR)

class Chain:
    def __init__(self, df, config_file="config/config.yaml"):
        # Load configuration from the YAML file
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)

        # Set up instance variables from the configuration
        self.df = df
        self.project_id = config["project"]["id"]
        self.region = config["project"]["region"]
        service_account_file = config["google"]["service_account_file"]
        llm_model = config["llm"]["model"]
        cache_maxsize = config["cache"]["maxsize"]
        cache_ttl = config["cache"]["ttl"]

        # Initialize credentials and environment variables
        credentials = initialize_google()
        print(f"Authenticated with service account: {credentials.service_account_email}")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_file

        # Initialize LLM and cache with loaded configuration values
        self.llm = ChatVertexAI(model=llm_model, credentials=credentials)
        self.model = GenerativeModel(f"{llm_model}-001")
        self.nutritional_parser = PydanticOutputParser(pydantic_object=NutritionFacts)
        self.health_recommendation_parser = PydanticOutputParser(pydantic_object=HealthRecommendation)
        self.cache = TTLCache(maxsize=cache_maxsize, ttl=cache_ttl)

    #### reference method for image analysis
    # def analyze_image(self):
    #     IMAGE_FILE = "data/product_photos/im1.png"
    #     image = Image.load_from_file(IMAGE_FILE)
    #     prompt_image_summary = "Explain the image"
    #     response = self.model.generate_content([prompt_image_summary, image])
    #     return response

    @traceable(name="extract_nutritional_info_from_image")
    def extract_nutritional_info(self, image):
        try:
            with PIL.Image.open(image) as img:
                buffer = io.BytesIO()
                img.save(buffer, format="PNG")
                image_bytes = buffer.getvalue()
            
            image = Image.from_bytes(image_bytes)
            prompt_nutritional_info = """
                Analyze the image of the food product and extract the following nutritional information:
                1. Product name and brand
                2. Serving size
                3. Calories per serving
                4. Macronutrients (protein, carbohydrates, fats) per serving
                5. Sugar content
                6. Sodium content
                7. Fiber content
                8. Vitamins and minerals (if available)
                9. List of ingredients
                10. Any health claims or certifications on the packaging

                Present the information in a structured format, focusing on accuracy and completeness.
                If any information is not visible or available, indicate that it's not provided.
                Please estimate the calories_per_serving on your own if not provided.
                Format the output using the following structure:
                {
                    "product_name": "Product name and brand",
                    "serving_size": "Serving size",
                    "calories_per_serving": "Calories per serving",
                    "macronutrients": {
                        "protein": "Protein content per serving",
                        "carbohydrates": "Carbohydrate content per serving",
                        "fats": "Fat content per serving"
                    },
                    "sugar_content": "Sugar content per serving",
                    "sodium_content": "Sodium content per serving",
                    "fiber_content": "Fiber content per serving",
                    "vitamins_and_minerals": "Vitamins and minerals per serving",
                    "ingredients": "List of ingredients",
                    "health_claims": "Health claims or certifications"
                }
                """
            cache_key = self._generate_cache_key(image_bytes)
            
            if cache_key in self.cache:
                print("Using cached response for extract_nutritional_info")
                return self.cache[cache_key]

            response = self.model.generate_content([prompt_nutritional_info, image])
            result = response.text
            self.cache[cache_key] = result
            return result
        except Exception as e:
            print(f"Error in extract_nutritional_info: {e}")
            return None
        finally:
            if img and isinstance(img, PIL.Image.Image) and img != image:
                img.close()
            # Close the buffer
            buffer.close()
    
    @traceable(name="calculate_expenditure_in_excercise")
    def calculate_expenditure_in_excercise(self, calories):
        prompt_calculate_excercise = f"""
        Provide a rough estimate of the time required to burn {calories} calories for an average adult doing moderate-intensity exercise. 
        Give only the estimates in this format, with no additional text:
        Format the output using the following structure:
        {{
            "cycling": "X minutes",
            "swimming": "Y minutes",
            "running": "Z minutes"
        }}
        """

        response = self.model.generate_content(prompt_calculate_excercise)
        return response.text
    
    @traceable(name="extract_calories_info_from_image")
    def extract_calories_info(self, image):
        img = PIL.Image.open(image)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        image = Image.from_bytes(buffer.getvalue())
        prompt_calories_count = """
           Please estimate the total calories in this image, assuming the food shown is a single serving for one person. 
           Provide a rough estimate of the calorie count, and break it down into approximate amounts of protein, carbohydrates, 
           and fats. Keep the estimates general, focusing on typical nutritional values for the types of 
           food visible in the image, without the need for precise measurements always give the preference to the lower side of the estimate.
           Format the output using the following structure:
           {
               "calories": "{calories}",
               "protein": "{protein}",
               "carbohydrates": "{carbohydrates}",
               "fats": "{fats}"
           }
           """

        response = self.model.generate_content([prompt_calories_count, image])
        return response.text
    
    @staticmethod    # Function to convert non-serializable types to JSON-friendly types
    def convert_types(obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):  # Convert numpy arrays to lists
            return obj.tolist()
        elif isinstance(obj, dict):
            return {key: Chain.convert_types(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [Chain.convert_types(item) for item in obj]
        return obj

    #### TODO: update prompt for meal summary, make it more instructive
    @traceable(name="assess_health_compatibility")
    def assess_health_compatibility(self, health_record, nutritional_info, meals_summary, preferences, target_nutrients):
        prompt = ChatPromptTemplate.from_template(
            "Analyze the compatibility of a food product with a user's health profile and dietary habits. "
            "Use the following information:\n\n"
            "1. Nutritional Information: {nutritional_info}\n"
            "2. User's Health Record: {health_record}\n"
            "3. User's Meals Summary: {meals_summary}\n"
            "4. User's Preferences: {preferences}\n"
            "5. User's Target Nutrients: {target_nutrients}\n\n"
            "Provide a comprehensive assessment addressing the following points:\n"
            "1. Product Suitability: Is the product suitable for the user based on their health record and preferences?\n"
            "2. Processing Level: Evaluate how processed the product is and its nutrient density.\n"
            "3. Nutritional Concerns: Assess if the product is high in fats, sugar, sodium, or calories relative to the user's needs and target nutrients.\n"
            "4. Ingredient Safety: Identify any potentially harmful or allergenic ingredients.\n"
            "5. Calorie Balance: Compare the product's calories to the user's daily intake from the meals summary and target calories.\n"
            "6. Nutritional Balance: Evaluate how the product's nutrients complement or conflict with nutrients already consumed and target nutrients.\n"
            "7. Health Impact: Discuss potential positive or negative effects on the user's health conditions.\n"
            "8. Recommendations: Suggest portion sizes or alternatives if necessary.\n\n"
            "Format your response as follows:\n"
            "- Suitability: [Brief statement on overall suitability]\n"
            "- Nutritional Analysis: [Detailed analysis of points 2-6]\n"
            "- Health Considerations: [Analysis of point 7]\n"
            "- Recommendations: [Actionable advice based on the analysis]\n"
            "- Sources: [List relevant nutritional or medical sources used for this assessment]\n\n"
            "Ensure your response is evidence-based, balanced, and tailored to the user's specific health profile, dietary habits, and target nutrients."
        )
        # Apply the conversion function to each dictionary entry
        combined_input = json.dumps(self.convert_types({
            "health_record": health_record,
            "nutritional_info": nutritional_info,
            "meals_summary": meals_summary,
            "preferences": preferences,
            "target_nutrients": target_nutrients
        }), sort_keys=True)

        cache_key = combined_input

        if cache_key in self.cache:
            print("Using cached response for assess_health_compatibility")
            return self.cache[cache_key]

        chain = prompt | self.llm 
        result = chain.invoke({
            "health_record": health_record,
            "nutritional_info": nutritional_info,
            "meals_summary": meals_summary,
            "preferences": preferences,
            "target_nutrients": target_nutrients
        })
        self.cache[cache_key] = result
        return result
    
    # Extract health summary from a health record
    @traceable(name="extract_nutritional_info_from_image")
    def get_health_summary(self, health_record):
        prompt = ChatPromptTemplate.from_template(
            "Given the following health record, extract a concise summary of the patient's "
            "key health concerns, dietary restrictions, and allergies that are relevant for "
            "assessing food product suitability. Focus on information that could impact nutritional recommendations.\n\n"
            "Health Record: {health_record}\n\n"
            "Provide the output as a structured summary."
        )
        chain = prompt | self.llm
        return chain.invoke({"health_record": health_record})
    
    # helper function to analyze meal pattern and suggest improvements
    @traceable(name="analyze_meal_pattern_and_suggest_improvements")
    def habit_analysis_with_suggestions(self, meal_data, timestamp):
        prompt = ChatPromptTemplate.from_template(
            """We are building a health app. Given user behavior/meal logs, analyze the behavior, identify patterns, 
            common mistakes/bad habits, and good habits the user has. We want to nudge the user with notifications 
            and encourage them to stay consistent with their good habits, motivate them to avoid repeating bad habits, 
            and provide suggestions to improve, including alternatives to their less healthy meal choices.
            Given the current timestamp {timestamp}, generate the following output:
            1. Notifications: Create sample notifications for 10am, 2pm, and 6:30 pm today. Each notification should be 
               encouraging, specific to the user's habits, and offer a practical suggestion.
            2. Habit Analysis: Provide a detailed analysis of the user's meal patterns, including:
               - Identified patterns for each meal (breakfast, lunch, dinner, snacks)
               - Good habits observed
               - Areas for improvement
               - Specific suggestions for healthier choices
            Meal Pattern Data: {meal_data}
            Provide the output as a structured summary in markdown format:
            "Patterns Identified:\n...
            \n\nGood Habits:\n...
            \n\nAreas for Improvement:\n...
            \n\nSuggestions:\n...
            \n\nNotifications:10:00 AM Notification: ...,2:00 PM Notification: ...,6:30 PM Notification: ..."
            """
        )
        chain = prompt | self.llm
        result = chain.invoke({"meal_data": meal_data, "timestamp": timestamp})
        return result.content
    
    # Compute the daily calorie/ nutrient intake of the user from health record
    @traceable(name="get_daily_intake")
    def get_daily_intake(self, health_record):
        prompt = ChatPromptTemplate.from_template(
            "Given the following health record, using medical conditions, height, weight, age, gender, activity level, "
            "key health concerns, dietary restrictions, of the user, compute the daily calorie/ nutrient intake of the user. "
            "Estimate how much calories,protein, carbohydrates, fats, sugar, sodium, fiber, vitamins, minerals, and water the user should consume daily. \n\n"
            "Health Record: {health_record}\n\n"
            "Provide the output as a structured summary."
        )
        chain = prompt | self.llm
        return chain.invoke({"health_record": health_record})

    @traceable(name="assess_pros_cons")
    def assess_pros_cons(self, nutritional_info):
        prompt = ChatPromptTemplate.from_template(
            "Given the following nutritional information, "
            "assess the pros and cons of the product. "
            "Nutritional Information: {nutritional_info}\n"
            "How processed and nutrient deficit is the product? "
            "Is it high in fats, sugar, sodium, calories? "
            "Are harmful ingredients present? "
            "If the product is highly processed, list the pros as almost negligible."
        )
        chain = prompt | self.llm
        return chain.invoke({"nutritional_info": nutritional_info})

    def process_nutrition_and_health(self, image, user_id=None, meals_summary=None):
        nutritional_info = self.extract_nutritional_info(image)
        
        if user_id is None or self.df.empty or 'user_id' not in self.df.columns:
            print("Warning: Unable to retrieve health record. User ID is None or DataFrame is invalid.")
            return None

        user_records = self.df.loc[self.df['user_id'] == user_id, 'health_record']
        if user_records.empty:
            print(f"Warning: No health record found for user_id: {user_id}")
            health_record = "No health record available"
        else:
            health_record = user_records.iloc[0] if len(user_records) > 0 else "No health record available"

        user_preferences = self.df.loc[self.df['user_id'] == user_id, 'preferences']
        if user_preferences.empty:
            print(f"Warning: No preferences found for user_id: {user_id}")
            preferences = "No preferences available"
        else:
            preferences = user_preferences.iloc[0] if len(user_preferences) > 0 else "No preferences available"

        user_target_nutrients = self.df.loc[self.df['user_id'] == user_id, 'target_nutrients']
        if user_target_nutrients.empty:
            print(f"Warning: No target nutrients found for user_id: {user_id}")
            target_nutrients = "No target nutrients available"
        else:
            target_nutrients = user_target_nutrients.iloc[0] if len(user_target_nutrients) > 0 else "No target nutrients available"

        recs = self.assess_health_compatibility(health_record, nutritional_info, meals_summary, preferences, target_nutrients)
        if isinstance(recs, AIMessage):
            recommendations_content = recs.content
        else:
            recommendations_content = recs 
        return recommendations_content,nutritional_info
    
    def calculate_calories(self, image, user_id=None):
        nutritional_info = self.extract_calories_info(image)
        print("checking nutritional info   ", nutritional_info)
        if user_id is None or self.df.empty or 'user_id' not in self.df.columns:
            print("Warning: Unable to retrieve health record. User ID is None or DataFrame is invalid.")
            return None

        if isinstance(nutritional_info, AIMessage):
            recommendations_content = nutritional_info.content
        else:
            recommendations_content = nutritional_info 
        return recommendations_content

    def print_nutritional_info(self, image):
        nutritional_info = self.extract_nutritional_info(image)
        return {"nutritional_info": nutritional_info}
    
    def calculate_exercise(self, calories=None):
        excercise = self.calculate_expenditure_in_excercise(calories)
        print("excercises ", excercise)
        return excercise
    
    def _generate_cache_key(self, input):
        """
        Generate a unique cache key based on the input string.
        """
        if isinstance(input, str):
            input = input.encode('utf-8')
        image_hash = hashlib.sha256(input).hexdigest()
        key = f"{image_hash}"
        return key