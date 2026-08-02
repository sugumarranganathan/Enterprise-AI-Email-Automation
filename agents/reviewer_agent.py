"""
Reviewer Agent

Reviews and improves the generated email before sending.
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm
from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are a Senior Enterprise Email Reviewer.

Your responsibility is to review the generated customer email.

Review Checklist:

1. Correct grammar and spelling.
2. Improve sentence structure.
3. Make the tone professional, polite, and empathetic.
4. Ensure the email is clear and easy to understand.
5. Remove repetitive or unnecessary sentences.
6. Ensure the response is consistent with the provided company knowledge and policy.
7. Do not invent information that is not present in the draft.
8. Preserve the original meaning and intent.
9. Keep the email concise but complete.
10. Do not include explanations or review comments.

Return ONLY the final improved email.
"""

        ),

        (

            "human",

            """
Review and improve the following email.

Draft Email:

{draft}
"""

        )

    ]

)


chain = prompt | llm


def reviewer_agent(state):

    logger.info("===== Reviewer Agent Started =====")

    result = chain.invoke(

        {

            "draft": state.get("draft_reply", "")

        }

    )

    state["reviewed_reply"] = result.content.strip()

    logger.info("===== Reviewer Agent Completed =====")

    return state
