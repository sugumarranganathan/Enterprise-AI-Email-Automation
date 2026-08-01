"""
Sentiment Agent
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm

from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
Identify the sentiment.

Return ONLY

Positive

Neutral

Negative

Angry
"""

        ),

        (

            "human",

            "{email}"

        )

    ]

)


chain = prompt | llm


def sentiment_agent(state):

    logger.info("Sentiment Agent Started")

    result = chain.invoke(

        {

            "email": state["email"]

        }

    )

    state["sentiment"] = result.content.strip()

    return state
