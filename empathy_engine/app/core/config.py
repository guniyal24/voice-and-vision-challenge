import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "The Empathy Engine"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    
    AUDIO_DIR: str = os.path.join(os.getcwd(), "data")

    EMOTION_MODEL_ID: str = "j-hartmann/emotion-english-distilroberta-base"

    class Config:
        case_sensitive = True

settings = Settings()
os.makedirs(settings.AUDIO_DIR, exist_ok=True)
