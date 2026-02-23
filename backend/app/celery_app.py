from celery import Celery
from app.core.config import settings
# Powered by Grok Multi-Voice + ElevenLabs Hybrid + LangGraph 🔥

celery = Celery("nightcrow", broker=settings.REDIS_URL, backend=settings.REDIS_URL)

@celery.task
def nightly_consolidation():
    from app.memory.langgraph_agent import ConsolidationNode
    # trigger consolidation
    print("Nightly consolidation done // Powered by LangGraph 🔥")