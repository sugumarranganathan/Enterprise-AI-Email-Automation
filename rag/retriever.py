"""
Retriever

Retrieves relevant documents from the Qdrant vector database.
"""

from rag.vectorstore import vectorstore
from utils.logger import logger


logger.info("Initializing Retriever...")


retriever = vectorstore.as_retriever(

    search_kwargs={

        "k": 3

    }

)


def retrieve(question: str):

    """
    Retrieve relevant documents.

    Parameters
    ----------
    question : str
        User query.

    Returns
    -------
    list
        List of relevant LangChain Document objects.
    """

    logger.info("=" * 60)
    logger.info("===== Retriever Started =====")
    logger.info("=" * 60)

    try:

        logger.info(f"Query : {question}")

        documents = retriever.invoke(question)

        logger.info(f"Retrieved {len(documents)} document(s).")

        logger.info("=" * 60)
        logger.info("===== Retriever Completed =====")
        logger.info("=" * 60)

        return documents

    except Exception as e:

        logger.exception("Retriever failed.")

        logger.info("=" * 60)
        logger.info("===== Retriever Completed =====")
        logger.info("=" * 60)

        return []
