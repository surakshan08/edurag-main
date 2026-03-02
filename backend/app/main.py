from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router
from app.state import state
from bootstrap import initialize_chatbot

app = FastAPI(
    title="EduRAG API",
    description="Campus Information RAG Service",
    version="1.0.0"
)

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    state.chatbot = initialize_chatbot()

app.include_router(router)