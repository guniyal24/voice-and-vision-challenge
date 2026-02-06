from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from app.models.schemas import TTSRequest, TTSResponse
from app.services.emotion import emotion_service
from app.services.audio import audio_service
import os

router = APIRouter()

def remove_file(path: str):
    """Background task to cleanup audio files after serving"""
    try:
        os.remove(path)
    except Exception:
        pass

@router.post("/synthesize", response_class=FileResponse)
async def synthesize_speech(request: TTSRequest, background_tasks: BackgroundTasks):
    """
    1. Analyzes text sentiment.
    2. Modulates voice parameters.
    3. Returns binary audio file directly.
    """
    try:
        emotion, score, _ = emotion_service.analyze(request.text)
   
        file_path, params = await audio_service.generate_emotional_audio(request.text, emotion)
        
        background_tasks.add_task(remove_file, file_path)
        
        headers = {
            "X-Detected-Emotion": emotion,
            "X-Emotion-Confidence": str(score),
            "X-Modulation-Pitch": str(params['pitch']),
            "X-Modulation-Speed": str(params['rate']),
            "X-Modulation-Volume": str(params['volume'])
        }
        
        return FileResponse(
            file_path, 
            media_type="audio/mpeg", 
            filename=f"speech_{emotion}.mp3",
            headers=headers
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze_only", response_model=TTSResponse)
async def analyze_only(request: TTSRequest):
    """Debug endpoint to check logic without generating audio"""
    emotion, score, _ = emotion_service.analyze(request.text)
    _, params = audio_service._map_emotion_to_prosody(emotion)
    return TTSResponse(
        download_url="N/A",
        detected_emotion=emotion,
        modulations_applied=params
    )