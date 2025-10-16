from pydantic import BaseModel, Field
from typing import List

class KubestronautPredictionRequest(BaseModel):
    theory_hours: int = Field(..., gt=0, description="Number of hours spent on theory")
    lab_hours: int = Field(..., gt=0, description="Number of hours spent on laboratory")
    number_full_exam_done: int = Field(..., ge=1, description="Number of full exams done")
    cncf_try_numbers: int = Field(..., gt=0, description="CNCF's Real exam attempts")
    location: str = Field(..., description="Location (urban, suburban, rural)")
    born_year: int = Field(..., ge=1800, le=2023, description="Year the Kubestronaut was born")
    selfassessment: str = Field(..., description="Self assessment of the Kubestronaut candidate (e.g., Good, Excellent, Fair)")

class PredictionResponse(BaseModel):
    predicted_final_result: float
    confidence_interval: List[float]
    features_importance: dict
    prediction_time: str