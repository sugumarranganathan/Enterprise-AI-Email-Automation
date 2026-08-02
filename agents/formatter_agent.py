"""
Formatter Agent

Create the final professional email.
"""

from langchain_core.prompts import ChatPromptTemplate

from utils.groq_client import llm
from utils.logger import logger


prompt = ChatPromptTemplate.from_messages(

    [

        (

            "system",

            """
You are an Enterprise Email Formatter.

Your responsibility is to convert the reviewed email into a final
professional customer email.

Instructions:

1. Create a clear and relevant Subject line.
2. Add a professional greeting.
3. Keep the original message unchanged unless formatting improvements
   are required.
4. Improve paragraph spacing and readability.
5. Preserve all company policy information.
6. Do NOT invent any new information.
7. Do NOT remove important information.
8. Add a professional closing.
9. Add the signature:

Customer Support Team

Return ONLY the final email.

Format:

Subject: ...

Dear Customer,

...

Kind Regards,

Customer Support Team
"""

        ),

        (

            "human",

            """
Reviewed Email

{reply}
"""

        )

    ]

)


chain = prompt | llm


def formatter_agent(state):

    logger.info("===== Formatter Agent Started =====")

    result = chain.invoke(

        {

            "reply": state.get("reviewed_reply", "")

        }

    )

    state["final_email"] = result.content.strip()

    logger.info("===== Formatter Agent Completed =====")

    return state
