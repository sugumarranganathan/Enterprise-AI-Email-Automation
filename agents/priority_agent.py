"""
Priority Detection Agent
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm

from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
Determine the priority.

Possible values:

High

Medium

Low

Urgent

Return only one word.
"""

        ),

        (

            "human",

            "{email}"

        )

    ]

)


chain = prompt | llm


def priority_agent(state):

    logger.info("Priority Agent Started")

    result = chain.invoke(

        {

            "email": state["email"]

        }

    )

    state["priority"] = result.content.strip()

    return state
