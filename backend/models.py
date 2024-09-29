from langchain_core.pydantic_v1 import BaseModel
from typing import Optional, List

class NutritionalInfo(BaseModel):
    calories: int
    total_fat: float
    saturated_fat: float
    trans_fat: float
    cholesterol: int
    sodium: int
    total_carbohydrate: int
    dietary_fiber: int
    total_sugars: int
    protein: int
    # Add any other nutritional fields you want to extract

    
class NutritionFacts(BaseModel):
    serving_size: Optional[str] = None
    calories: Optional[int] = None
    total_fat: Optional[str] = None
    saturated_fat: Optional[str] = None
    trans_fat: Optional[str] = None
    cholesterol: Optional[str] = None
    sodium: Optional[str] = None
    total_carbohydrate: Optional[str] = None
    dietary_fiber: Optional[str] = None
    total_sugar: Optional[str] = None
    protein: Optional[str] = None
    vitamin_d: Optional[str] = None
    calcium: Optional[str] = None
    iron: Optional[str] = None
    potassium: Optional[str] = None

class NutrientAssessment(BaseModel):
    nutrient: Optional[str] = None
    value: Optional[float] = None
    unit: Optional[str] = None
    daily_value_percentage: Optional[int] = None
    assessment: Optional[str] = None

class NutritionalAnalysis(BaseModel):
    pros: Optional[List[str]] = None
    cons: Optional[List[str]] = None
    processing_assessment: Optional[str] = None
    nutrient_deficit_assessment: Optional[str] = None
    high_content_assessment: Optional[dict] = None
    harmful_ingredients_assessment: Optional[str] = None
    key_nutrients: Optional[List[NutrientAssessment]] = None
    conclusion: Optional[str] = None
    missing_information: Optional[List[str]] = None

class HealthRecommendation(BaseModel):
    nutritional_analysis: Optional[NutritionalAnalysis] = None