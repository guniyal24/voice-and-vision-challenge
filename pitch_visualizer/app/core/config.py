import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "The Pitch Visualizer"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    
    # OpenAI Key (Optional - triggers fallback if missing)
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # Path to store generated images (used for fallback engine)
    IMAGE_DIR: str = os.path.join(os.getcwd(), "static", "generated")

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
os.makedirs(settings.IMAGE_DIR, exist_ok=True)
