"""
Responder Agent

Generate a professional email reply using
summary, intent, retrieved knowledge,
and company policy.
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm
from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are an Enterprise Customer Support Email Assistant.

Your job is to write a professional customer email.

Rules:

1. Use ONLY the provided Company Knowledge and Policy.
2. Do NOT invent information.
3. If information is missing, politely mention that additional verification is required.
4. Write in a professional, friendly and empathetic tone.
5. Never mention internal systems, AI, RAG or company documents.
6. Do not include a subject line.
7. Start with an appropriate greeting.
8. End with a professional closing.
9. If the customer reports a problem, apologize appropriately.
10. If company policy contains instructions, follow them exactly.

The email should be well formatted and ready to send.
"""

        ),

        (

            "human",

            """
Customer Email Summary:
{summary}

Customer Intent:
{intent}

Relevant Company Knowledge:
{knowledge}

Relevant Company Policy:
{policy}

Write a complete professional email reply.
"""

        )

    ]

)


chain = prompt | llm


def responder_agent(state):

    logger.info("===== Responder Agent Started =====")

    result = chain.invoke(

        {

            "summary": state.get("summary", ""),

            "intent": state.get("intent", ""),

            "knowledge": state.get("retrieved_context", ""),

            "policy": state.get("policy_result", "")

        }

    )

    state["draft_reply"] = result.content

    logger.info("===== Responder Agent Completed =====")

    return state
