"""
====================================================
Responder Agent

Generates a professional customer email
using:

- Summary
- Intent
- Retrieved Knowledge
- Company Policy

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
You are an Enterprise Customer Support Email Assistant.

Your responsibility is to generate a
professional customer email.

Instructions:

1. Use ONLY the supplied Company Knowledge
   and Company Policy.

2. Never invent information.

3. If information is unavailable,
   politely mention that additional
   verification is required.

4. Maintain a professional,
   empathetic and friendly tone.

5. Never mention:
   - AI
   - LLM
   - RAG
   - Vector Database
   - Internal systems
   - Internal documentation

6. Do NOT include a subject line.

7. Start with a professional greeting.

8. End with a professional closing.

9. If the customer reports a problem,
   apologize appropriately.

10. If a policy applies,
    follow it exactly.

Return ONLY the email body.
"""

        ),

        (

            "human",

            """
Customer Email Summary
----------------------

{summary}


Customer Intent
---------------

{intent}


Company Knowledge
-----------------

{knowledge}


Company Policy
--------------

{policy}


Write the complete professional email.
"""

        )

    ]

)


# =====================================================
# Chain
# =====================================================

chain = prompt | llm


# =====================================================
# Responder Agent
# =====================================================

def responder_agent(state):

    logger.info("=" * 60)
    logger.info("Responder Agent Started")
    logger.info("=" * 60)

    summary = state.get("summary", "")
    intent = state.get("intent", "")
    knowledge = state.get("retrieved_context", "")
    policy = state.get("policy_result", "")

    try:

        response = chain.invoke(

            {

                "summary": summary,

                "intent": intent,

                "knowledge": knowledge,

                "policy": policy,

            }

        )

        draft = response.content.strip()

        if not draft:

            draft = (
                "Dear Customer,\n\n"
                "Thank you for contacting us.\n\n"
                "We are reviewing your request and will "
                "get back to you shortly.\n\n"
                "Kind regards,\n"
                "Customer Support Team"
            )

    except Exception:

        logger.exception("Responder Agent failed.")

        draft = (
            "Dear Customer,\n\n"
            "Thank you for contacting us.\n\n"
            "We are unable to generate a response at "
            "this time. Our support team will review "
            "your request and respond shortly.\n\n"
            "Kind regards,\n"
            "Customer Support Team"
        )

    # =====================================================
    # Save Workflow State
    # =====================================================

    state["draft_reply"] = draft
    state["response"] = draft

    logger.info("Professional email generated successfully.")

    logger.info("=" * 60)
    logger.info("Responder Agent Completed")
    logger.info("=" * 60)

    return state
