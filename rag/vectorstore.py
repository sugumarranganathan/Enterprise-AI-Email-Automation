"""
====================================================
Qdrant Vector Store

Supports:
- Google Colab
- Render
- Local Development
====================================================
"""

from langchain_qdrant import QdrantVectorStore

from rag.embeddings import embeddings
from tools.qdrant_tool import client
from utils.config import settings


# =====================================================
# Create Vector Store
# =====================================================

vectorstore = QdrantVectorStore(
    client=client,
    collection_name=settings.QDRANT_COLLECTION,
    embedding=embeddings,
)


# =====================================================
# Retriever
# =====================================================

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": 3
    }
)


# =====================================================
# Manual Test
# =====================================================

if __name__ == "__main__":

    print("✅ Vector Store Loaded")
    print("Collection :", settings.QDRANT_COLLECTION)

    try:
        docs = retriever.invoke("test")
        print(f"Retrieved {len(docs)} documents")

    except Exception as e:
        print("Retriever Test Failed")
        print(e)
