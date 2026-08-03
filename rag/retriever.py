"""
====================================================
Retriever

Retrieves relevant documents from the
Qdrant Vector Database.

Supports:
- Google Colab
- Render
- Local Development
====================================================
"""

from rag.vectorstore import retriever
from utils.logger import logger


logger.info("Retriever initialized successfully.")


def retrieve(query: str):
    """
    Retrieve relevant documents from Qdrant.

    Parameters
    ----------
    query : str
        User question.

    Returns
    -------
    list
        List of LangChain Document objects.
    """

    logger.info("=" * 60)
    logger.info("Knowledge Retrieval Started")
    logger.info("=" * 60)

    try:

        query = query.strip()

        if not query:

            logger.warning("Empty query received.")

            return []

        logger.info(f"Query : {query}")

        docs = retriever.invoke(query)

        logger.info(f"Retrieved {len(docs)} document(s).")

        logger.info("=" * 60)
        logger.info("Knowledge Retrieval Completed")
        logger.info("=" * 60)

        return docs

    except Exception:

        logger.exception("Knowledge retrieval failed.")

        logger.info("=" * 60)
        logger.info("Knowledge Retrieval Failed")
        logger.info("=" * 60)

        return []


# =====================================================
# Manual Test
# =====================================================

if __name__ == "__main__":

    documents = retrieve("refund policy")

    print("=" * 60)

    print(f"Retrieved : {len(documents)} document(s)")

    print("=" * 60)

    if documents:

        print(documents[0].page_content)
