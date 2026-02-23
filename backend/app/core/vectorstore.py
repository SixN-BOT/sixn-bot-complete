from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
# Powered by Grok Multi-Voice + ElevenLabs Hybrid + LangGraph 🔥

Base = declarative_base()

class NightMemory(Base):
    __tablename__ = "night_memories"
    id = Column(Integer, primary_key=True)
    content = Column(String)
    embedding = Column(Vector(1536))
    score = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)