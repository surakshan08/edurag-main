from typing import List, Dict


class TextChunker:
    """Handles document chunking with overlap."""

    def __init__(self, chunk_size: int = 400, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_documents(self, documents: List[Dict]) -> List[Dict]:
        chunks = []

        for idx, doc in enumerate(documents):
            chunks.append({
                "chunk_id": idx,
                "content": doc["content"],
                "category": doc["category"],
                "metadata": {
                    "source": "college_data",
                    "doc_id": idx
                }
            })

        return chunks