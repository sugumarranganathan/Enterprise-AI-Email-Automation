"""
Email Sender Agent
"""

from tools.gmail_sender import send_email

from utils.logger import logger


def email_sender(state):

    logger.info("Sending Email...")

    send_email(

        to_email=state["sender"],

        subject="Re: " + state["subject"],

        body=state["final_email"],
        thread_id=state["thread_id"]

    )

    state["send_status"] = "Sent"

    return state
