from pydantic import BaseModel
from typing import List, Optional

class StoryRequest(BaseModel):
    text: str
    style: str = "cinematic"  # cinematic, anime, watercolor, cyberpunk

class StoryPanel(BaseModel):
    panel_id: int
    original_text: str
    enhanced_prompt: str
    image_url: str
    engine_used: str

class StoryResponse(BaseModel):
    panels: List[StoryPanel]
    total_panels: int
