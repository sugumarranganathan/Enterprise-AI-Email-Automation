"""
Knowledge Agent
"""

from rag.retriever import retrieve

from utils.logger import logger


def knowledge_agent(state):

    logger.info("Knowledge Agent Started")

    docs = retrieve(state["email"])

    context = "\n\n".join(

        [

            doc.page_content

            for doc in docs

        ]

    )

    state["retrieved_context"] = context

    return state
