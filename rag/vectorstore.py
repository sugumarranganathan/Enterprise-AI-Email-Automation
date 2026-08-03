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

    embedding=embeddings

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
# Helper Function
# =====================================================

def similarity_search(query: str, k: int = 3):
    """
    Search similar documents.

    Parameters
    ----------
    query : str
        User query.

    k : int
        Number of documents.

    Returns
    -------
    list
        LangChain Document objects.
    """

    return vectorstore.similarity_search(

        query,

        k=k

    )


# =====================================================
# Manual Test
# =====================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Qdrant Vector Store")
    print("=" * 60)

    print("Collection :", settings.QDRANT_COLLECTION)

    try:

        docs = similarity_search("test")

        print(f"Retrieved {len(docs)} document(s).")

        if docs:

            print()

            print(docs[0].page_content[:300])

    except Exception as e:

        print("Vector Store Test Failed")

        print(e)
