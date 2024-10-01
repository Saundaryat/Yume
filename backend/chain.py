import json
from langchain_google_vertexai import ChatVertexAI
from langchain.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import PydanticOutputParser
from models import NutritionalInfo, HealthRecommendation, NutritionFacts
from langchain_google_vertexai import VertexAI
from langchain.schema import AIMessage 
from vertexai.vision_models import ImageTextModel
import io
import PIL

from vertexai.preview.generative_models import GenerativeModel, Image

class Chain:
    def __init__(self, df):
        self.df = df
        self.llm = ChatVertexAI(model="gemini-1.5-pro")
        self.model = GenerativeModel("gemini-1.5-pro-001")
        self.nutritional_parser = PydanticOutputParser(pydantic_object=NutritionFacts)
        self.health_recommendation_parser = PydanticOutputParser(pydantic_object=HealthRecommendation)

    #### reference method for image analysis
    # def analyze_image(self):
    #     IMAGE_FILE = "data/product_photos/im1.png"
    #     image = Image.load_from_file(IMAGE_FILE)
    #     prompt_image_summary = "Explain the image"
    #     response = self.model.generate_content([prompt_image_summary, image])
    #     return response

    def extract_nutritional_info(self, image):
        img = PIL.Image.open(image)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        image = Image.from_bytes(buffer.getvalue())
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
            The output should be a JSON object with the following structure:
            {
                "product_name": "Product name and brand",
                "serving_size": "Serving size",
                "calories_per_serving": "Calories per serving",
                "macronutrients": {
                    "protein": "Protein content per serving",
                    "carbohydrates": "Carbohydrate content per serving",
                    "fats": "Fat content per    serving"
                },
                "sugar_content": "Sugar content per serving",
                "sodium_content": "Sodium content per serving",
                "fiber_content": "Fiber content per serving",
                "vitamins_and_minerals": "Vitamins and minerals per serving",
                "ingredients": "List of ingredients",
                "health_claims": "Health claims or certifications"
            }
            """

        response = self.model.generate_content([prompt_nutritional_info, image])
        return response.text

    def assess_health_compatibility(self, health_record, nutritional_info):
        prompt = ChatPromptTemplate.from_template(
            "Given the following health record and nutritional information, "
            "assess whether the product is suitable for the user. "
            "How processed and nutrient deficit is the product?"
            "Is it high in fats, sugar, sodium, calories?"
            "Are Harmful Ingredients present?"
            "Nutritional Information: {nutritional_info}\n"
            "Health Record: {health_record}\n"
            "Provide the sources as well for the recommendations"
            "Provide the output as a string."
        )
        chain = prompt | self.llm 
        return chain.invoke({
            "health_record": health_record,
            "nutritional_info": nutritional_info
        })
    
    # Extract health summary from a health record
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

    def process_nutrition_and_health(self, image, user_id=None):
        nutritional_info = self.extract_nutritional_info(image)
        # print("checking reccomendations   ", nutritional_info)
        if user_id is None or self.df.empty or 'user_id' not in self.df.columns:
            print("Warning: Unable to retrieve health record. User ID is None or DataFrame is invalid.")
            return None

        user_records = self.df.loc[self.df['user_id'] == user_id, 'health_record']
        
        if user_records.empty:
            print(f"Warning: No health record found for user_id: {user_id}")
            return None

        health_record = user_records.iloc[0]
        recs = self.assess_health_compatibility(health_record, nutritional_info)
        if isinstance(recs, AIMessage):
            recommendations_content = recs.content
        else:
            recommendations_content = recs 
        return recommendations_content

    def print_nutritional_info(self, image):
        nutritional_info = self.extract_nutritional_info(image)
        return {"nutritional_info": nutritional_info}
    
