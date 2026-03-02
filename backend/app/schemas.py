from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):
    query: str


class Source(BaseModel):
    category: str
    distance: float


class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: List[Source]