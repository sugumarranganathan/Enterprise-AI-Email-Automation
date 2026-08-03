"""
====================================================
Email Sender Agent

Sends the final email using Gmail API.

Supports:
- Google Colab
- Render
- Local Development
====================================================
"""

from datetime import datetime

from tools.gmail_sender import send_email
from utils.logger import logger


# =====================================================
# Email Sender Agent
# =====================================================

def email_sender(state):

    logger.info("=" * 60)
    logger.info("Email Sender Agent Started")
    logger.info("=" * 60)

    # =====================================================
    # Read Workflow State
    # =====================================================

    to_email = str(
        state.get("sender", "")
    ).strip()

    subject = str(
        state.get("subject", "Customer Support")
    ).strip()

    body = str(
        state.get("final_email", "")
    ).strip()

    thread_id = state.get("thread_id")

    approval_status = state.get(
        "approval_status",
        "Approved"
    )

    auto_send = state.get(
        "auto_send",
        True
    )

    # =====================================================
    # Human Approval Check
    # =====================================================

    if not auto_send:

        logger.warning(
            "Email requires human approval."
        )

        state["send_status"] = "Pending Approval"
        state["message_id"] = None
        state["send_error"] = (
            "Waiting for human approval."
        )
        state["sent_time"] = None

        logger.info("=" * 60)
        logger.info("Email Sender Agent Completed")
        logger.info("=" * 60)

        return state

    # =====================================================
    # Validation
    # =====================================================

    if not to_email:

        logger.warning("Recipient email missing.")

        state["send_status"] = "Failed"
        state["send_error"] = "Recipient email missing."

        return state

    if not body:

        logger.warning("Final email is empty.")

        state["send_status"] = "Failed"
        state["send_error"] = "Email body is empty."

        return state

    if not subject:

        subject = "Customer Support"

    # =====================================================
    # Send Email
    # =====================================================

    try:

        logger.info(f"Recipient : {to_email}")
        logger.info(f"Subject   : Re: {subject}")

        response = send_email(

            to_email=to_email,

            subject=f"Re: {subject}",

            body=body,

            thread_id=thread_id,

        )

        state["send_status"] = "Sent"

        state["message_id"] = response.get("id")

        state["thread_id"] = response.get(
            "threadId",
            thread_id
        )

        state["sent_time"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        state["send_error"] = None

        logger.info("Email sent successfully.")

        logger.info(
            f"Message ID : {state['message_id']}"
        )

    except FileNotFoundError:

        logger.warning(
            "Gmail credentials not found."
        )

        state["send_status"] = "Skipped"

        state["message_id"] = None

        state["sent_time"] = None

        state["send_error"] = (
            "Gmail credentials not configured."
        )

    except Exception as e:

        logger.exception(
            "Email sending failed."
        )

        state["send_status"] = "Failed"

        state["message_id"] = None

        state["sent_time"] = None

        state["send_error"] = str(e)

    # =====================================================
    # Save Additional Information
    # =====================================================

    state["email_sent"] = (
        state["send_status"] == "Sent"
    )

    state["approval_status"] = approval_status

    # =====================================================
    # Logging
    # =====================================================

    logger.info(f"Send Status : {state['send_status']}")

    logger.info("=" * 60)
    logger.info("Email Sender Agent Completed")
    logger.info("=" * 60)

    return state
