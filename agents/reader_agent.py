"""
Reader Agent

Extracts:
- Summary
- Intent
- Action Items
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm
from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are an Email Reader Agent.

Read the email carefully.

Return your answer in exactly this format:

SUMMARY:
...

INTENT:
...

ACTION ITEMS:
...
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

    logger.info("Reader Agent Started")

    result = chain.invoke(

        {

            "email": state["email"]

        }

    )

    output = result.content

    state["summary"] = output

    state["intent"] = output

    state["action_items"] = output

    return state
