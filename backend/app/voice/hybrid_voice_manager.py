from app.voice.grok_voice_client import GrokVoiceClient
from app.voice.elevenlabs_voice import ElevenLabsVoiceClient
from app.core.config import settings
# Powered by Grok Multi-Voice + Imagine Video + Vision + LangGraph + ElevenLabs Hybrid 🔥

class HybridVoiceManager:
    def __init__(self):
        self.grok = GrokVoiceClient()      # ton ancien multi
        self.eleven = ElevenLabsVoiceClient()
        self.mode = "elevenlabs" if settings.USE_ELEVENLABS else "grok"  # config switch

    async def connect(self, guild_id: str, voice_client: VoiceClient, voice_name: str = "Eve"):
        if self.mode == "elevenlabs":
            await self.eleven.connect_realtime(guild_id, voice_client, voice_id="your_eleven_voice_id")
        else:
            await self.grok.connect_session(guild_id, voice_client, voice_name)

    async def send_text(self, guild_id: str, text: str):
        if self.mode == "elevenlabs":
            await self.eleven.speak(guild_id, text)
        else:
            # Grok speech-to-speech logic
            pass

hybrid_manager = HybridVoiceManager()