from pydantic_settings import BaseSettings
# Powered by Grok Multi-Voice + ElevenLabs Hybrid + LangGraph 🔥

class Settings(BaseSettings):
    XAI_API_KEY: str
    ELEVENLABS_API_KEY: str
    DISCORD_TOKEN: str
    DATABASE_URL: str
    REDIS_URL: str
    USE_ELEVENLABS: bool = True

    class Config:
        env_file = ".env"

settings = Settings()