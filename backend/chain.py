import json
from langchain_google_vertexai import ChatVertexAI
from langchain.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import PydanticOutputParser
from models import NutritionalInfo, HealthRecommendation, NutritionFacts
from langchain_google_vertexai import VertexAI

class Chain:
    def __init__(self, df):
        self.df = df
        self.llm = ChatVertexAI(model="gemini-1.5-pro")
        self.vision_model = VertexAI(model_name="gemini-pro-vision")
        self.nutritional_parser = PydanticOutputParser(pydantic_object=NutritionFacts)
        self.health_recommendation_parser = PydanticOutputParser(pydantic_object=HealthRecommendation)

    def extract_nutritional_info(self, image):
        prompt = ChatPromptTemplate.from_template(
            "Extract all nutritional information from this image of a nutrition facts table. "
            "Provide the output in a structured format in JSON convert all the values to string."
        )
        chain = prompt | self.vision_model | self.nutritional_parser
        return chain.invoke({"image": image})

    def assess_health_compatibility(self, health_record, nutritional_info):
        prompt = ChatPromptTemplate.from_template(
            "Given the following health record and nutritional information, "
            "assess whether the product is suitable for the user. "
            "Health Record: {health_record}\n"
            "Nutritional Information: {nutritional_info}\n"
            "How processed and nutrient deficit is the product?"
            "Is it high in fats, sugar, sodium, calories?"
            "Are Harmful Ingredients present?"
            "Provide the output in a structured format in JSON"
        )
        chain = prompt | self.llm | self.health_recommendation_parser
        return chain.invoke({
            "health_record": health_record,
            "nutritional_info": nutritional_info.model_dump_json()
        })

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

    def process_nutrition_and_health(self, image, health_record):
        nutritional_info = self.extract_nutritional_info(image)
        print("checking reccomendations   ", nutritional_info)
        #recommendation = self.assess_health_compatibility(health_record, nutritional_info)
        reccomendations = self.assess_pros_cons(nutritional_info)
        print("checking reccomendations   ", reccomendations)
        return {
            "nutritional_info": nutritional_info,
            "health_recommendation": reccomendations
        }

