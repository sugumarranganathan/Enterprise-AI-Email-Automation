"""
Formatter Agent

Create final email.
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm
from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
Format the email professionally.

Include

Subject

Greeting

Body

Closing

Signature

Return the final email only.
"""

        ),

        (

            "human",

            "{reply}"

        )

    ]

)


chain = prompt | llm


def formatter_agent(state):

    logger.info("Formatter Agent Started")

    result = chain.invoke(

        {

            "reply": state["reviewed_reply"]

        }

    )

    state["final_email"] = result.content

    return state
