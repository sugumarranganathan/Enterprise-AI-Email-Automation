"""
Qdrant Vector Store
"""

from langchain_qdrant import QdrantVectorStore

from rag.embeddings import embeddings

from tools.qdrant_tool import client

from utils.config import settings


vectorstore = QdrantVectorStore(

    client=client,

    collection_name=settings.QDRANT_COLLECTION,

    embedding=embeddings

)
