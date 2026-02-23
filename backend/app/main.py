from fastapi import FastAPI
from app.core.config import settings
from app.voice.hybrid_voice_manager import hybrid_manager
import discord
from discord.ext import commands, tasks
import asyncio

app = FastAPI(title="NightCrow Crow Manager v2.6")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# 4 Bots personas (Luna, Kai, Mia, Neo)
PERSONAS = {
    "luna": {"voice": "Eve", "color": 0xFF69B4},
    "kai": {"voice": "Leo", "color": 0x00BFFF},
    "mia": {"voice": "Ara", "color": 0xFF1493},
    "neo": {"voice": "Rex", "color": 0x32CD32}
}

@app.get("/")
async def root():
    return {"status": "NightCrow Crow Manager v2.6 live // Powered by Grok + ElevenLabs 🔥"}

@app.post("/voice/join/{guild_id}/{bot_name}")
async def join_voice(guild_id: str, bot_name: str):
    # Crow Manager route vers le bon bot
    await hybrid_manager.connect(guild_id, bot_name)
    return {"status": f"{bot_name} joined voice"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)