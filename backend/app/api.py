from fastapi import APIRouter, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.state import state
from bootstrap import initialize_chatbot

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):

    # Lazy load chatbot
    if state.chatbot is None:
        state.chatbot = initialize_chatbot()

    result = state.chatbot.query(payload.query)
    return result