"""
Knowledge Retrieval Tool
"""

from langchain_qdrant import QdrantVectorStore

from rag.embeddings import embeddings
from tools.qdrant_tool import client
from utils.config import settings

vectorstore = QdrantVectorStore(
    client=client,
    collection_name=settings.QDRANT_COLLECTION,
    embedding=embeddings,
)

def search_knowledge(query: str, k: int = 3) -> str:
    docs = vectorstore.similarity_search(query, k=k)

    if not docs:
        return "No relevant knowledge found."

    return "\n\n".join(doc.page_content for doc in docs)
