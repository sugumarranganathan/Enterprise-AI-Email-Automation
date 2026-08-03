"""
====================================================
Formatter Agent

Formats the reviewed email into the final
professional customer email.

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
You are an Enterprise Email Formatter.

Your responsibility is to prepare the
FINAL customer email.

Formatting Rules:

1. Create a short, professional Subject line.

2. Add a professional greeting.

3. Preserve the reviewed email content.

4. Improve paragraph spacing.

5. Improve readability.

6. Do NOT invent information.

7. Do NOT remove important information.

8. Preserve company policy wording.

9. End with a professional closing.

10. Use this signature exactly:

Kind Regards,

Customer Support Team

Return ONLY the final email.

Example:

Subject: Order Update

Dear Customer,

Thank you for contacting us.

......

Kind Regards,

Customer Support Team
"""

        ),

        (

            "human",

            """
Reviewed Email

----------------

{reply}

"""

        )

    ]

)


# =====================================================
# Chain
# =====================================================

chain = prompt | llm


# =====================================================
# Formatter Agent
# =====================================================

def formatter_agent(state):

    logger.info("=" * 60)
    logger.info("Formatter Agent Started")
    logger.info("=" * 60)

    reviewed_reply = state.get(
        "reviewed_reply",
        ""
    ).strip()

    if not reviewed_reply:

        logger.warning("Reviewed email is empty.")

        state["final_email"] = ""

        logger.info("=" * 60)
        logger.info("Formatter Agent Completed")
        logger.info("=" * 60)

        return state

    try:

        response = chain.invoke(

            {

                "reply": reviewed_reply

            }

        )

        final_email = response.content.strip()

        if not final_email:

            final_email = reviewed_reply

    except Exception:

        logger.exception("Formatter Agent failed.")

        final_email = reviewed_reply

    # =====================================================
    # Save Workflow State
    # =====================================================

    state["final_email"] = final_email

    logger.info("Professional email formatted successfully.")

    logger.info("=" * 60)
    logger.info("Formatter Agent Completed")
    logger.info("=" * 60)

    return state
