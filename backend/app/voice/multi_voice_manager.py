import asyncio
import json
import base64
import os
from typing import Dict
import websockets
from discord import VoiceClient, FFmpegPCMAudio
from pydub import AudioSegment
from app.core.config import settings

# Powered by Grok Multi-Voice + Imagine Video + Vision + LangGraph 🔥

class MultiVoiceManager:
    def __init__(self):
        self.sessions: Dict[str, dict] = {}
        self.semaphore = asyncio.Semaphore(8)

    async def connect(self, guild_id: str, voice_client: VoiceClient, voice: str = "Eve"):
        async with self.semaphore:
            if guild_id in self.sessions:
                await self.disconnect(guild_id)
            uri = "wss://api.x.ai/v1/realtime"
            headers = {"Authorization": f"Bearer {settings.XAI_API_KEY}"}
            ws = await websockets.connect(uri, extra_headers=headers)
            await ws.send(json.dumps({"type": "session.update", "voice": voice, "sample_rate": 16000}))
            task = asyncio.create_task(self._loop(guild_id, ws, voice_client))
            self.sessions[guild_id] = {"ws": ws, "vc": voice_client, "task": task, "voice": voice}
            print(f"✅ MultiVoice Session STARTED {guild_id} → {voice}")

    async def _loop(self, guild_id, ws, vc):
        try:
            async for msg in ws:
                data = json.loads(msg)
                if data.get("type") == "audio":
                    audio_b64 = data["audio"]
                    raw = base64.b64decode(audio_b64)
                    seg = AudioSegment.from_raw(raw, sample_width=2, frame_rate=16000, channels=1)
                    seg.export("/tmp/out.opus", format="opus")
                    vc.play(FFmpegPCMAudio("/tmp/out.opus"))
        except:
            pass
        finally:
            await self.disconnect(guild_id)

    async def send_audio(self, guild_id: str, pcm: bytes):
        if guild_id in self.sessions:
            b64 = base64.b64encode(pcm).decode()
            await self.sessions[guild_id]["ws"].send(json.dumps({"type": "audio", "data": b64}))

    async def disconnect(self, guild_id: str):
        if guild_id in self.sessions:
            s = self.sessions[guild_id]
            s["task"].cancel()
            await s["ws"].close()
            del self.sessions[guild_id]
            print(f"❌ Session closed {guild_id}")

manager = MultiVoiceManager()