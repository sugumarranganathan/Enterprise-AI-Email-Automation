"""
Email Sender Agent

Send the final email using Gmail.
"""

from datetime import datetime

from tools.gmail_sender import send_email
from utils.logger import logger


def email_sender(state):

    logger.info("=" * 60)
    logger.info("===== Email Sender Agent Started =====")
    logger.info("=" * 60)

    try:

        # =====================================================
        # Read Workflow State
        # =====================================================

        to_email = state.get("sender", "").strip()
        subject = state.get("subject", "").strip()
        body = state.get("final_email", "").strip()
        thread_id = state.get("thread_id")

        # =====================================================
        # Validation
        # =====================================================

        if not to_email:
            raise ValueError("Recipient email is missing.")

        if not body:
            raise ValueError("Final email body is empty.")

        if not subject:
            subject = "Customer Support"

        logger.info(f"Recipient : {to_email}")
        logger.info(f"Subject   : Re: {subject}")

        if thread_id:
            logger.info(f"Thread ID : {thread_id}")
        else:
            logger.info("Thread ID : New Conversation")

        # =====================================================
        # Send Email
        # =====================================================

        response = send_email(
            to_email=to_email,
            subject=f"Re: {subject}",
            body=body,
            thread_id=thread_id,
        )

        # =====================================================
        # Success
        # =====================================================

        state["send_status"] = "Sent"
        state["message_id"] = response.get("id")
        state["thread_id"] = response.get("threadId", thread_id)
        state["sent_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        state["send_error"] = None

        logger.info("Email sent successfully.")
        logger.info(f"Message ID : {state['message_id']}")

    except FileNotFoundError:

        logger.warning("Gmail credentials not configured.")
        logger.warning("Skipping email sending.")

        state["send_status"] = "Skipped"
        state["message_id"] = None
        state["thread_id"] = thread_id
        state["sent_time"] = None
        state["send_error"] = "Gmail credentials not configured."

    except ValueError as e:

        logger.warning(str(e))

        state["send_status"] = "Skipped"
        state["message_id"] = None
        state["thread_id"] = thread_id
        state["sent_time"] = None
        state["send_error"] = str(e)

    except Exception as e:

        logger.exception("Unexpected error while sending email.")

        state["send_status"] = "Failed"
        state["message_id"] = None
        state["thread_id"] = thread_id
        state["sent_time"] = None
        state["send_error"] = str(e)

    logger.info("=" * 60)
    logger.info("===== Email Sender Agent Completed =====")
    logger.info("=" * 60)

    return state
