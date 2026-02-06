import httpx
import os
import uuid
import urllib.parse
from openai import AsyncOpenAI
from app.core.config import settings

class ImageService:
    def __init__(self):
        self.openai_client = None
        if settings.OPENAI_API_KEY and settings.OPENAI_API_KEY.startswith("sk-"):
            self.openai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    async def generate_image(self, prompt: str) -> tuple[str, str]:

        if self.openai_client:
            try:
                response = await self.openai_client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                )
                return response.data[0].url, "DALL-E 3 (High Quality)"
            except Exception as e:
                print(f"OpenAI Error (Falling back to free engine): {e}")
  
        return await self._generate_fallback(prompt)

    async def _generate_fallback(self, prompt: str) -> tuple[str, str]:
        """
        Free, unlimited generation using Stable Diffusion via Pollinations.
        """
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&seed={uuid.uuid4().int}"
        
        filename = f"{uuid.uuid4()}.jpg"
        filepath = os.path.join(settings.IMAGE_DIR, filename)
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, timeout=30.0)
                if response.status_code == 200:
                    with open(filepath, "wb") as f:
                        f.write(response.content)
                    return f"/static/generated/{filename}", "Stable Diffusion (Free Tier)"
                else:
                    return "https://via.placeholder.com/1024?text=Generation+Failed", "Error"
            except Exception as e:
                print(f"Fallback Error: {e}")
                return "https://via.placeholder.com/1024?text=Error", "Error"

image_service = ImageService()
