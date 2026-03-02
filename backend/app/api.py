from fastapi import APIRouter, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.state import state

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    if state.chatbot is None:
        raise HTTPException(status_code=503, detail="Chatbot not initialized")

    result = state.chatbot.query(payload.query)
    return result