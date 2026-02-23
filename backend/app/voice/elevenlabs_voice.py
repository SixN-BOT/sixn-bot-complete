import asyncio
import json
import base64
from elevenlabs.client import ElevenLabs
from elevenlabs import stream
from discord import VoiceClient, FFmpegPCMAudio
from app.core.config import settings
import websockets
# Powered by Grok Multi-Voice + Imagine Video + Vision + LangGraph + ElevenLabs Hybrid 🔥

class ElevenLabsVoiceClient:
    def __init__(self):
        self.client = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)
        self.active_sessions = {}

    async def connect_realtime(self, guild_id: str, voice_client: VoiceClient, voice_id: str = "21m00Tcm4TlvDq8ikWAM"):
        uri = f"wss://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream-input?model_id=eleven_turbo_v2"
        async with websockets.connect(uri) as ws:
            self.active_sessions[guild_id] = ws
            await ws.send(json.dumps({"text": " ", "voice_settings": {"stability": 0.75, "similarity_boost": 0.85}}))
            asyncio.create_task(self._handle_stream(guild_id, ws, voice_client))

    async def _handle_stream(self, guild_id, ws, voice_client):
        try:
            async for message in ws:
                data = json.loads(message)
                if data.get("audio"):
                    audio_bytes = base64.b64decode(data["audio"])
                    # Stream direct to Discord VC
                    with open("/tmp/temp.opus", "wb") as f:
                        f.write(audio_bytes)
                    voice_client.play(FFmpegPCMAudio("/tmp/temp.opus"))
        except Exception as e:
            print(f"ElevenLabs error {guild_id}: {e}")

    async def speak(self, guild_id: str, text: str):
        if guild_id in self.active_sessions:
            await self.active_sessions[guild_id].send(json.dumps({"text": text, "flush": True}))