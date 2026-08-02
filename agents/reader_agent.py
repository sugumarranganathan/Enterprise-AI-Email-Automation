"""
Reader Agent

Reads an email and extracts:
- Summary
- Intent
- Action Items
"""

import json

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm
from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are an Enterprise Email Reader Agent.

Read the email carefully.

Return ONLY valid JSON.

Example:

{
    "summary": "...",
    "intent": "...",
    "action_items": "..."
}

Do not return markdown.
Do not use ```json.
Do not add explanations.
"""

        ),

        (

            "human",

            "{email}"

        )

    ]

)


chain = prompt | llm


def reader_agent(state):

    logger.info("===== Reader Agent Started =====")

    try:

        email = state.get("email", "")

        if not email:
            raise ValueError("Email content is empty.")

        result = chain.invoke(

            {

                "email": email

            }

        )

        data = json.loads(result.content)

        state["summary"] = data.get("summary", "")
        state["intent"] = data.get("intent", "")
        state["action_items"] = data.get("action_items", "")

        logger.info(f"Summary : {state['summary']}")
        logger.info(f"Intent  : {state['intent']}")

    except Exception as e:

        logger.exception("Reader Agent Failed")

        state["summary"] = ""
        state["intent"] = ""
        state["action_items"] = ""
        state["reader_error"] = str(e)

    logger.info("===== Reader Agent Completed =====")

    return state
