"""
Policy Agent

(Current Version)

Later this agent will:

Read company policies

Check compliance

Return policy decisions
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm

from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are a Company Policy Agent.

Read the email summary.

Determine whether any company policy
should be considered.

If none,

return

No Policy Required

Otherwise explain briefly.
"""

        ),

        (

            "human",

            "{summary}"

        )

    ]

)


chain = prompt | llm


def policy_agent(state):

    logger.info("Policy Agent Started")

    result = chain.invoke(

        {

            "summary": state["summary"]

        }

    )

    state["policy_result"] = result.content

    return state
