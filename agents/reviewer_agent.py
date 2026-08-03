"""
====================================================
Reviewer Agent

Reviews and improves the generated email
before approval.

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
You are a Senior Enterprise Email Reviewer.

Your responsibility is to review and improve
the generated customer email.

Review Rules:

1. Correct grammar and spelling.

2. Improve sentence structure.

3. Maintain a professional,
   polite and empathetic tone.

4. Make the email concise
   and easy to understand.

5. Remove duplicate or
   unnecessary sentences.

6. Preserve the original meaning.

7. Do NOT invent information.

8. Do NOT change company policy.

9. Do NOT mention AI,
   internal systems,
   knowledge base,
   or review process.

10. Return ONLY the final email.

"""

        ),

        (

            "human",

            """
Review the following draft email.

Draft Email

----------------

{draft}

"""

        )

    ]

)


# =====================================================
# Chain
# =====================================================

chain = prompt | llm


# =====================================================
# Reviewer Agent
# =====================================================

def reviewer_agent(state):

    logger.info("=" * 60)
    logger.info("Reviewer Agent Started")
    logger.info("=" * 60)

    draft = state.get("draft_reply", "").strip()

    if not draft:

        logger.warning("Draft reply is empty.")

        state["reviewed_reply"] = ""

        logger.info("=" * 60)
        logger.info("Reviewer Agent Completed")
        logger.info("=" * 60)

        return state

    try:

        response = chain.invoke(

            {

                "draft": draft

            }

        )

        reviewed = response.content.strip()

        if not reviewed:

            reviewed = draft

    except Exception:

        logger.exception("Reviewer Agent failed.")

        reviewed = draft

    # =====================================================
    # Save Workflow State
    # =====================================================

    state["reviewed_reply"] = reviewed

    logger.info("Email reviewed successfully.")

    logger.info("=" * 60)
    logger.info("Reviewer Agent Completed")
    logger.info("=" * 60)

    return state
