from pydantic import BaseModel
from typing import Optional, Dict

class TTSRequest(BaseModel):
    text: str
    class Config:
        json_schema_extra = {
            "example": {
                "text": "I am so incredibly happy that we finally succeeded!"
            }
        }

class EmotionResponse(BaseModel):
    primary_emotion: str
    confidence_score: float
    meta_data: Dict[str, float]

class TTSResponse(BaseModel):
    download_url: str
    detected_emotion: str
    modulations_applied: Dict[str, float]
