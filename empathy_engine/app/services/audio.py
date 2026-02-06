import os
import uuid
import edge_tts
from app.core.config import settings

class AudioService:
    
    def _map_emotion_to_prosody(self, emotion: str):
   
        base_voice = "en-US-AriaNeural"
        
        mapping = {
            "joy": {
                "rate": "+20%",     # Speak faster/excitedly
                "pitch": "+15Hz",   # Higher pitch = happy
                "volume": "+10%"    # Louder
            },
            "surprise": {
                "rate": "+25%", 
                "pitch": "+20Hz", 
                "volume": "+15%"
            },
            "anger": {
                "rate": "+10%",     # Slightly faster (aggressive)
                "pitch": "-5Hz",    # Drop pitch slightly for authority
                "volume": "+30%"    # Much louder
            },
            "sadness": {
                "rate": "-15%",     # Slower
                "pitch": "-15Hz",   # Lower, somber pitch
                "volume": "-20%"    # Softer
            },
            "fear": {
                "rate": "+15%",     # Fast/Erratic
                "pitch": "+10Hz",   # Tense/Higher
                "volume": "+0%"
            },
            "neutral": {
                "rate": "+0%", 
                "pitch": "+0Hz", 
                "volume": "+0%"
            },
            "disgust": {
                "rate": "-10%", 
                "pitch": "-10Hz", 
                "volume": "-10%"
            }
        }
        
        params = mapping.get(emotion, mapping["neutral"])
        return base_voice, params

    async def generate_emotional_audio(self, text: str, emotion: str):
        """
        Generates audio using Microsoft Edge's Neural TTS.
        This is ASYNC because it communicates with the Edge API.
        """
        temp_id = str(uuid.uuid4())
        final_path = os.path.join(settings.AUDIO_DIR, f"{temp_id}.mp3")

        voice, params = self._map_emotion_to_prosody(emotion)
        

        communicate = edge_tts.Communicate(
            text, 
            voice, 
            rate=params["rate"], 
            pitch=params["pitch"], 
            volume=params["volume"]
        )
        
        # 3. Save to file
        await communicate.save(final_path)
            
        return final_path, params

audio_service = AudioService()