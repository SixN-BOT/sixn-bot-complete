import asyncio
import json
import base64
import websockets
from discord import VoiceClient, FFmpegPCMAudio
from pydub import AudioSegment
from app.core.config import settings
# Powered by Grok Multi-Voice + ElevenLabs Hybrid + LangGraph 🔥

class GrokVoiceClient:
    async def connect_session(self, guild_id: str, voice_client: VoiceClient, voice_name: str = "Eve"):
        uri = "wss://api.x.ai/v1/realtime"
        headers = {"Authorization": f"Bearer {settings.XAI_API_KEY}"}
        async with websockets.connect(uri, extra_headers=headers) as ws:
            await ws.send(json.dumps({"type": "session.update", "voice": voice_name}))
            # loop audio handling...
            print(f"Grok Voice connected for {guild_id}")