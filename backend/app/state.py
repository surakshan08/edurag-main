from typing import Optional
from rag.pipeline import CampusRAGChatbot


class AppState:
    chatbot: Optional[CampusRAGChatbot] = None


state = AppState()