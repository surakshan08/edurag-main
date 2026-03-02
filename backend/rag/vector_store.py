from typing import List, Dict, Tuple
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:
    """FAISS-based vector store for semantic search."""

    def __init__(self, embedding_model_name: str = "all-MiniLM-L6-v2"):
        self.embedder = SentenceTransformer(embedding_model_name)
        self.index = None
        self.chunks: List[Dict] = []
        self.dimension = 384

    def build_index(self, chunks: List[Dict]):
        self.chunks = chunks
        texts = [chunk["content"] for chunk in chunks]

        embeddings = self.embedder.encode(
            texts,
            show_progress_bar=True,
            convert_to_numpy=True
        ).astype("float32")

        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(embeddings)

    def search(self, query: str, k: int = 3) -> List[Tuple[Dict, float]]:
        if self.index is None:
            raise RuntimeError("FAISS index not initialized")

        query_embedding = self.embedder.encode(
            [query],
            convert_to_numpy=True
        ).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            results.append((self.chunks[idx], float(dist)))

        return results