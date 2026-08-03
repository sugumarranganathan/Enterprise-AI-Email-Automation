"""
====================================================
Knowledge Agent

Retrieves relevant knowledge from
Qdrant Vector Database.
====================================================
"""

from rag.retriever import retrieve
from utils.logger import logger


def knowledge_agent(state):
    """
    Retrieve company knowledge from Qdrant
    and store it in the workflow state.
    """

    logger.info("=" * 60)
    logger.info("Knowledge Agent Started")
    logger.info("=" * 60)

    # =====================================================
    # Build Query
    # =====================================================

    query = (
        state.get("intent")
        or state.get("email")
        or state.get("summary")
        or ""
    ).strip()

    if not query:

        logger.warning("No query available.")

        state["knowledge"] = ""
        state["retrieved_context"] = ""
        state["knowledge_docs"] = []

        logger.info("=" * 60)
        logger.info("Knowledge Agent Completed")
        logger.info("=" * 60)

        return state

    logger.info(f"Query: {query}")

    # =====================================================
    # Retrieve Documents
    # =====================================================

    try:

        docs = retrieve(query)

    except Exception:

        logger.exception("Knowledge retrieval failed.")

        docs = []

    # =====================================================
    # Build Context
    # =====================================================

    if docs:

        context = "\n\n".join(

            doc.page_content

            for doc in docs

            if hasattr(doc, "page_content")

        )

    else:

        context = "No relevant company knowledge found."

    # =====================================================
    # Save into Workflow State
    # =====================================================

    state["knowledge"] = context
    state["retrieved_context"] = context
    state["knowledge_docs"] = docs

    logger.info(f"Retrieved Documents : {len(docs)}")

    logger.info("=" * 60)
    logger.info("Knowledge Agent Completed")
    logger.info("=" * 60)

    return state
