import re
import json
from openai import OpenAI
from app.core.config import settings

class NLPService:
    def __init__(self):
        self.client = None
        if settings.OPENAI_API_KEY:
            self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def segment_text(self, text: str) -> list[str]:
        """
        Smart Segmentation Logic:
        1. (Primary) LLM-Based: Uses GPT-3.5 to intelligently group sentences based on visual context.
           It looks "forward and backward" to ensure every segment is a complete visual thought.
        2. (Fallback) Rule-Based: Uses regex but merges short, fragmented sentences.
        """
        if self.client:
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system", 
                            "content": (
                                "You are a Storyboard Director. Your job is to split the user's narrative text into "
                                "3 to 5 distinct visual scenes. "
                                "Rules:\n"
                                "1. Group short related sentences together (e.g., 'He jumped. It was high' -> 'He jumped high').\n"
                                "2. Ensure every segment has enough context to generate a standalone image.\n"
                                "3. If a character is mentioned (e.g., 'Bob the Robot'), ensure their identity is clear in every segment if needed.\n"
                                "4. Return ONLY a raw JSON list of strings. No markdown."
                            )
                        },
                        {"role": "user", "content": text}
                    ],
                    temperature=0.3, 
                )
                
                content = response.choices[0].message.content.strip()
    
                if content.startswith("```json"):
                    content = content.replace("```json", "").replace("```", "")
                
                segments = json.loads(content)
                
                if isinstance(segments, list) and len(segments) >= 1:
                    return segments
            except Exception as e:
                print(f"LLM Segmentation failed ({e}). Falling back to heuristic.")

        return self._heuristic_segmentation(text)

    def _heuristic_segmentation(self, text: str) -> list[str]:

        raw_segments = re.split(r'(?<=[.!?])\s+', text.strip())
        raw_segments = [s.strip() for s in raw_segments if s.strip()]
        
        if not raw_segments:
            return []

        merged_segments = []
        current_segment = ""

        for i, segment in enumerate(raw_segments):
            # If current buffer is empty, start new
            if not current_segment:
                current_segment = segment
            else:
   
                if len(current_segment) < 50 or len(segment) < 40:
                    current_segment += " " + segment
                else:

                    merged_segments.append(current_segment)
                    current_segment = segment
        
        if current_segment:
            merged_segments.append(current_segment)

        if len(merged_segments) < 3 and len(raw_segments) >= 3:
            return raw_segments[-3:]
            
        return merged_segments

    def enhance_prompt(self, segment: str, style: str) -> str:
        """
        Requirement 3: Intelligent Prompt Engineering.
        Wraps the basic text in artistic modifiers based on the selected style.
        """
        style_modifiers = {
            "cinematic": "cinematic shot, 35mm film, bokeh, dramatic lighting, 8k, highly detailed, movie still, color graded",
            "anime": "anime style, Studio Ghibli, Makoto Shinkai, vibrant colors, detailed background, 4k, cell shaded",
            "cyberpunk": "cyberpunk city, neon lights, rain, futuristic, high tech, blade runner vibes, volumetric lighting",
            "pixar": "3d render, pixar style, disney animation, cute, vibrant, volumetric lighting, c4d, unreal engine",
            "watercolor": "watercolor painting, soft brush strokes, artistic, pastel colors, white background, illustration"
        }
        
        modifiers = style_modifiers.get(style, style_modifiers["cinematic"])
        
        # We add "visual" keywords to ensure the AI knows we want a scene, not text
        return f"Visual scene: {segment}. Art style: {modifiers}"

nlp_service = NLPService()