from typing import Dict
from .vector_store import VectorStore
from .generator import LLMGenerator


class CampusRAGChatbot:
    """Complete RAG pipeline for campus information."""

    def __init__(
        self,
        embedding_model: str = "all-MiniLM-L6-v2",
        llm_model: str = "google/flan-t5-base",
        top_k: int = 3
    ):
        self.vector_store = VectorStore(embedding_model)
        self.generator = LLMGenerator(llm_model)
        self.top_k = top_k

    def setup(self, chunks):
        self.vector_store.build_index(chunks)

    def query(self, question: str) -> Dict:
        results = self.vector_store.search(question, k=self.top_k)

        context_parts = []
        sources = []

        for chunk, score in results:
            context_parts.append(chunk["content"])
            sources.append({
                "category": chunk["category"],
                "distance": score
            })

        context = "\n\n".join(context_parts)
        answer = self.generator.generate_answer(question, context)

        return {
            "question": question,
            "answer": answer,
            "sources": sources
        }