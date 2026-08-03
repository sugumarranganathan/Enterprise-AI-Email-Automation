"""
====================================================
Gmail Reader Utility

Read the latest email from Gmail.
====================================================
"""

import base64

from googleapiclient.discovery import build

from tools.gmail_auth import get_gmail_credentials
from utils.logger import logger


def read_latest_email():
    """
    Read the latest email from Gmail.
    """

    logger.info("=" * 60)
    logger.info("===== Gmail Reader Started =====")
    logger.info("=" * 60)

    try:

        # =====================================================
        # Gmail Authentication
        # =====================================================

        creds = get_gmail_credentials()

        service = build(
            "gmail",
            "v1",
            credentials=creds
        )

        # =====================================================
        # Read Latest Email
        # =====================================================

        results = service.users().messages().list(
            userId="me",
            maxResults=1,
            labelIds=["INBOX"]
        ).execute()

        messages = results.get("messages", [])

        if not messages:

            logger.warning("Inbox is empty.")

            logger.info("=" * 60)
            logger.info("===== Gmail Reader Completed =====")
            logger.info("=" * 60)

            return None

        # =====================================================
        # Get Email Details
        # =====================================================

        message = service.users().messages().get(
            userId="me",
            id=messages[0]["id"],
            format="full"
        ).execute()

        headers = message["payload"]["headers"]

        sender = ""
        subject = ""

        for header in headers:

            if header["name"] == "From":
                sender = header["value"]

            elif header["name"] == "Subject":
                subject = header["value"]

        # =====================================================
        # Extract Body
        # =====================================================

        body = ""

        payload = message["payload"]

        if "parts" in payload:

            for part in payload["parts"]:

                if part.get("mimeType") == "text/plain":

                    data = part["body"].get("data")

                    if data:

                        body = base64.urlsafe_b64decode(
                            data
                        ).decode("utf-8", errors="ignore")

                    break

        else:

            data = payload.get("body", {}).get("data")

            if data:

                body = base64.urlsafe_b64decode(
                    data
                ).decode("utf-8", errors="ignore")

        logger.info("Latest email read successfully.")

        logger.info("=" * 60)
        logger.info("===== Gmail Reader Completed =====")
        logger.info("=" * 60)

        return {
            "sender": sender,
            "subject": subject,
            "email": body,
            "thread_id": message.get("threadId"),
            "message_id": message.get("id")
        }

    except FileNotFoundError:

        logger.warning("Gmail credentials not configured.")
        logger.warning("Skipping Gmail Reader.")

        return None

    except Exception:

        logger.exception("Failed to read Gmail.")

        return None


# =====================================================
# Backward Compatibility
# =====================================================

def read_emails():
    """
    Alias for older code.
    Keeps existing imports working.
    """
    return read_latest_email()
