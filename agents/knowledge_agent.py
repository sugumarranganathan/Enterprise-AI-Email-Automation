"""
Knowledge Agent

Retrieve relevant knowledge from Qdrant.
"""

from rag.retriever import retrieve
from utils.logger import logger


def knowledge_agent(state):

    logger.info("===== Knowledge Agent Started =====")

    # Prefer intent; fall back to email
    query = (
        state.get("intent")
        or state.get("email")
        or ""
    )

    if not query:
        logger.warning("No query available for knowledge retrieval.")
        state["knowledge"] = ""
        return state

    docs = retrieve(query)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    state["knowledge"] = context

    logger.info(f"Retrieved {len(docs)} document(s).")
    logger.info("===== Knowledge Agent Completed =====")

    return state
