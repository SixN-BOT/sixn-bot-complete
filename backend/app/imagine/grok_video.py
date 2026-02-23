import httpx
from app.core.config import settings

async def generate_video(prompt: str, image_url=None, duration=10):
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.x.ai/v1/images/generations",
            headers={"Authorization": f"Bearer {settings.XAI_API_KEY}"},
            json={"model": "grok-imagine-video", "prompt": prompt, "image_url": image_url, "duration": duration, "with_audio": True}
        )
        return resp.json()["video_url"]  # MP4 direct