from fastapi import APIRouter, HTTPException
from app.models.schemas import StoryRequest, StoryResponse, StoryPanel
from app.services.nlp import nlp_service
from app.services.image_gen import image_service
import asyncio

router = APIRouter()

@router.post("/generate_storyboard", response_model=StoryResponse)
async def generate_storyboard(request: StoryRequest):
    """
    Main Pipeline:
    1. Segment Text (NLP)
    2. Enhance Prompts (Prompt Engineering)
    3. Generate Images (Hybrid AI Engine)
    4. Return structured Storyboard
    """
    try:

        segments = nlp_service.segment_text(request.text)
        
        tasks = []
        for i, segment in enumerate(segments):
            enhanced_prompt = nlp_service.enhance_prompt(segment, request.style)
            tasks.append(process_panel(i+1, segment, enhanced_prompt))
        
        panels = await asyncio.gather(*tasks)
            
        return StoryResponse(panels=panels, total_panels=len(panels))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def process_panel(index, text, prompt):
    image_url, engine = await image_service.generate_image(prompt)
    return StoryPanel(
        panel_id=index,
        original_text=text,
        enhanced_prompt=prompt,
        image_url=image_url,
        engine_used=engine
    )
