"""
Policy Agent

Analyzes the email summary and determines
whether company policies should be applied.
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm
from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Company Policy Agent.

Read the customer email summary.

Determine whether any company policy
should be considered.

If no policy is applicable, return:

No Policy Required

Otherwise provide a brief policy recommendation.
"""
        ),
        (
            "human",
            "{summary}"
        )
    ]
)

chain = prompt | llm


def policy_agent(state):

    logger.info("=" * 60)
    logger.info("===== Policy Agent Started =====")
    logger.info("=" * 60)

    summary = state.get("summary", "")

    if not summary:

        logger.warning("Summary is missing.")

        state["policy"] = "No Policy Required"
        state["policy_result"] = "No Policy Required"

        logger.info("=" * 60)
        logger.info("===== Policy Agent Completed =====")
        logger.info("=" * 60)

        return state

    result = chain.invoke(
        {
            "summary": summary
        }
    )

    policy = result.content.strip()

    # Save using both keys for compatibility
    state["policy"] = policy
    state["policy_result"] = policy

    logger.info("Policy generated successfully.")

    logger.info("=" * 60)
    logger.info("===== Policy Agent Completed =====")
    logger.info("=" * 60)

    return state
