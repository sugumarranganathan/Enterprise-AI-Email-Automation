"""
====================================================
Policy Agent

Determines which company policy should be
applied based on the customer email.

Supports:
- Google Colab
- Render
- Local Development
====================================================
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm
from utils.logger import logger


# =====================================================
# Prompt
# =====================================================

prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are the Company Policy Agent.

Your responsibility is to determine whether
company policies apply to the customer's request.

Rules:

1. Read the email summary carefully.

2. If a company policy applies,
   provide a short policy recommendation.

3. If no policy is required,
   respond exactly with:

No Policy Required

Keep the response concise and professional.
"""

        ),

        (

            "human",

            "{summary}"

        )

    ]

)


# =====================================================
# Chain
# =====================================================

chain = prompt | llm


# =====================================================
# Policy Agent
# =====================================================

def policy_agent(state):

    logger.info("=" * 60)
    logger.info("Policy Agent Started")
    logger.info("=" * 60)

    summary = (

        state.get("summary")

        or state.get("email")

        or ""

    ).strip()

    if not summary:

        logger.warning("Summary not available.")

        state["policy"] = "No Policy Required"
        state["policy_result"] = "No Policy Required"

        logger.info("=" * 60)
        logger.info("Policy Agent Completed")
        logger.info("=" * 60)

        return state

    try:

        response = chain.invoke(

            {

                "summary": summary

            }

        )

        policy = response.content.strip()

        if not policy:

            policy = "No Policy Required"

    except Exception:

        logger.exception("Policy generation failed.")

        policy = "No Policy Required"

    # =====================================================
    # Save into Workflow State
    # =====================================================

    state["policy"] = policy
    state["policy_result"] = policy

    logger.info(f"Policy : {policy}")

    logger.info("=" * 60)
    logger.info("Policy Agent Completed")
    logger.info("=" * 60)

    return state
