from langgraph.graph import StateGraph
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, add_messages
from datetime import datetime
from app.core.vectorstore import NightMemory
from app.core.redis import redis_client
# Powered by Grok Multi-Voice + ElevenLabs Hybrid + LangGraph 🔥

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    night_memories: list

graph = StateGraph(AgentState)
# ... tous les nodes ajoutés (input, vision, etc.)

async def ConsolidationNode(state):
    # scoring 5 facteurs
    strong_memories = []  # logic
    redis_client.publish("memories", "new_night_memories")
    state["night_memories"] = strong_memories
    return state

# compile graph