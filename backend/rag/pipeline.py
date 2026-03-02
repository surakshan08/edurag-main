from typing import Dict
from .vector_store import VectorStore
from .generator import LLMGenerator


class CampusRAGChatbot:
    """Complete RAG pipeline for campus information."""

    def __init__(
        self,
        embedding_model: str = "all-MiniLM-L6-v2",
        llm_model: str = "google/flan-t5-small",
        top_k: int = 2
    ):
        self.vector_store = VectorStore(embedding_model)
        self.generator = LLMGenerator(llm_model)
        self.top_k = top_k

    def setup(self, chunks):
        self.vector_store.build_index(chunks)

    def query(self, question: str) -> Dict:
    results = self.vector_store.search(question, k=self.top_k)

    # 🔎 Filter low-relevance chunks
    filtered_results = []
    for chunk, score in results:
        if score < 1.2:   # you can tune this threshold
            filtered_results.append((chunk, score))

    if not filtered_results:
        return {
            "question": question,
            "answer": "The information is not available in the provided college data.",
            "sources": []
        }

    context_parts = []
    sources = []

    for chunk, score in filtered_results:
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