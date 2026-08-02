"""
Email Listener Agent

Reads the latest unread email from Gmail
and stores all required information in the workflow state.
"""

from datetime import datetime

from tools.gmail_reader import read_latest_email

from utils.logger import logger


def email_listener(state):

    logger.info("===== Email Listener Started =====")

    try:

        email = read_latest_email()

        if not email:
            logger.warning("No unread emails found.")

            state["email_found"] = False
            state["listener_error"] = "No unread emails."

            logger.info("===== Email Listener Completed =====")

            return state

        # -------------------------------------------------
        # Store Email Details
        # -------------------------------------------------

        state["sender"] = email.get("sender", "")
        state["subject"] = email.get("subject", "")
        state["email"] = email.get("email", "")
        state["thread_id"] = email.get("thread_id")
        state["message_id"] = email.get("message_id")

        state["email_found"] = True
        state["listener_error"] = None
        state["received_time"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # -------------------------------------------------
        # Logging
        # -------------------------------------------------

        logger.info(f"Sender      : {state['sender']}")
        logger.info(f"Subject     : {state['subject']}")
        logger.info(f"Thread ID   : {state['thread_id']}")
        logger.info(f"Message ID  : {state['message_id']}")

    except Exception as e:

        logger.exception("Email Listener Failed.")

        state["email_found"] = False
        state["listener_error"] = str(e)

    logger.info("===== Email Listener Completed =====")

    return state
