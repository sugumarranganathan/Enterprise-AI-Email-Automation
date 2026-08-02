"""
Knowledge Agent

Retrieve relevant knowledge from the Qdrant Vector Database.
"""

from rag.retriever import retrieve
from utils.logger import logger


def knowledge_agent(state):

    logger.info("=" * 60)
    logger.info("===== Knowledge Agent Started =====")
    logger.info("=" * 60)

    # =====================================================
    # Query
    # =====================================================

    query = (
        state.get("intent")
        or state.get("email")
        or ""
    )

    if not query:

        logger.warning("No query available for retrieval.")

        state["knowledge"] = ""
        state["retrieved_context"] = ""

        logger.info("=" * 60)
        logger.info("===== Knowledge Agent Completed =====")
        logger.info("=" * 60)

        return state

    logger.info(f"Query : {query}")

    # =====================================================
    # Retrieve Documents
    # =====================================================

    docs = retrieve(query)

    if docs:

        context = "\n\n".join(
            doc.page_content
            for doc in docs
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
    logger.info("===== Knowledge Agent Completed =====")
    logger.info("=" * 60)

    return state
