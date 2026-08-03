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


def retrieve(query: str) -> str:
    """
    Retrieve relevant knowledge from Qdrant.

    Parameters
    ----------
    query : str
        User question.

    Returns
    -------
    str
        Retrieved context as a single string.
    """

    logger.info("=" * 60)
    logger.info("🔎 Knowledge Retrieval Started")
    logger.info("=" * 60)

    try:

        logger.info(f"Query: {query}")

        docs = retriever.invoke(query)

        logger.info(f"Retrieved {len(docs)} document(s).")

        if not docs:

            logger.warning("No relevant documents found.")

            return "No relevant knowledge found."

        context = "\n\n".join(

            doc.page_content

            for doc in docs

        )

        logger.info("=" * 60)
        logger.info("✅ Knowledge Retrieval Completed")
        logger.info("=" * 60)

        return context

    except Exception as e:

        logger.exception("Knowledge retrieval failed.")

        logger.info("=" * 60)
        logger.info("❌ Knowledge Retrieval Failed")
        logger.info("=" * 60)

        return "Knowledge retrieval failed."
