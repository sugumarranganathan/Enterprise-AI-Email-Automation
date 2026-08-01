"""
Reviewer Agent

Improve grammar
Professional tone
Compliance
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm
from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are a Senior Email Reviewer.

Review the draft.

Improve

Grammar

Tone

Professionalism

Return only the improved email.
"""

        ),

        (

            "human",

            "{draft}"

        )

    ]

)


chain = prompt | llm


def reviewer_agent(state):

    logger.info("Reviewer Agent Started")

    result = chain.invoke(

        {

            "draft": state["draft_reply"]

        }

    )

    state["reviewed_reply"] = result.content

    return state
