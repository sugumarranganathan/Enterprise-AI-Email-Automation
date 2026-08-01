"""
Responder Agent

Generate professional email reply.
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm
from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are a Professional Email Assistant.

Generate a professional reply.

Use

Summary

Intent

Company Context

Policy Result

Write only the email body.

Do not include subject.
"""

        ),

        (

            "human",

            """

Summary

{summary}

Intent

{intent}

Knowledge

{knowledge}

Policy

{policy}

"""

        )

    ]

)


chain = prompt | llm


def responder_agent(state):

    logger.info("Responder Agent Started")

    result = chain.invoke(

        {

            "summary": state["summary"],

            "intent": state["intent"],

            "knowledge": state["retrieved_context"],

            "policy": state["policy_result"]

        }

    )

    state["draft_reply"] = result.content

    return state
