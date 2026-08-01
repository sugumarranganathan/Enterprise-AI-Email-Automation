"""
Classification Agent
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm

from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are an Email Classification Agent.

Classify the email into ONE category.

Categories:

Sales

Support

HR

Finance

IT

Complaint

Feedback

General

Return ONLY the category.
"""

        ),

        (

            "human",

            "{email}"

        )

    ]

)


chain = prompt | llm


def classification_agent(state):

    logger.info("Classification Agent Started")

    result = chain.invoke(

        {

            "email": state["email"]

        }

    )

    state["category"] = result.content.strip()

    return state
