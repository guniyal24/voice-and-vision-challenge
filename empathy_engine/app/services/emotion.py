from transformers import pipeline
from app.core.config import settings
import logging

logger = logging.getLogger("uvicorn")

class EmotionService:
    def __init__(self):
        logger.info("Loading Emotion Classification Model...")
        self.classifier = pipeline(
            "text-classification", 
            model=settings.EMOTION_MODEL_ID, 
            top_k=None
        )
        logger.info("Model Loaded Successfully.")

    def analyze(self, text: str):
        results = self.classifier(text)[0]
        
        sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
        
        top_emotion = sorted_results[0]['label']
        top_score = sorted_results[0]['score']
        
        all_scores = {res['label']: res['score'] for res in results}
        
        return top_emotion, top_score, all_scores

emotion_service = EmotionService()