from rag.data_manager import CollegeDataManager
from rag.chunker import TextChunker
from rag.pipeline import CampusRAGChatbot


def initialize_chatbot():
    data = CollegeDataManager.create_sample_data()
    chunker = TextChunker()
    chunks = chunker.chunk_documents(data)

    chatbot = CampusRAGChatbot()
    chatbot.setup(chunks)

    return chatbot