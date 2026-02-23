from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
# Powered by Grok Multi-Voice + ElevenLabs Hybrid + LangGraph 🔥

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)