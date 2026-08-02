"""
Email Sender Agent

Send the final email using Gmail.
"""

from datetime import datetime

from tools.gmail_sender import send_email

from utils.logger import logger


def email_sender(state):

    logger.info("===== Email Sender Agent Started =====")

    try:

        # -------------------------------------------------
        # Read State
        # -------------------------------------------------

        to_email = state.get("sender", "")
        subject = state.get("subject", "")
        body = state.get("final_email", "")
        thread_id = state.get("thread_id")

        if not to_email:
            raise ValueError("Recipient email is missing.")

        if not body:
            raise ValueError("Final email body is empty.")

        logger.info(f"Recipient : {to_email}")
        logger.info(f"Subject   : Re: {subject}")

        # -------------------------------------------------
        # Send Email
        # -------------------------------------------------

        send_email(

            to_email=to_email,

            subject=f"Re: {subject}",

            body=body,

            thread_id=thread_id

        )

        # -------------------------------------------------
        # Update State
        # -------------------------------------------------

        state["send_status"] = "Sent"
        state["sent_time"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        state["send_error"] = None

        logger.info("Email sent successfully.")

    except Exception as e:

        logger.exception("Email sending failed.")

        state["send_status"] = "Failed"
        state["sent_time"] = None
        state["send_error"] = str(e)

    logger.info("===== Email Sender Agent Completed =====")

    return state
