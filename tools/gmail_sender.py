"""
Gmail Sender Utility

Send emails using the Gmail API.
Supports replying within an existing thread or
sending a new email.
"""

import base64

from email.mime.text import MIMEText

from googleapiclient.discovery import build

from tools.gmail_auth import get_gmail_credentials


def send_email(
    to_email: str,
    subject: str,
    body: str,
    thread_id: str | None = None,
):
    """
    Send an email.

    Parameters
    ----------
    to_email : str
        Recipient email address.

    subject : str
        Email subject.

    body : str
        Plain-text email body.

    thread_id : str | None
        Gmail thread ID.
        If provided, the email is sent as a reply.
        Otherwise, it starts a new conversation.
    """

    creds = get_gmail_credentials()

    service = build(
        "gmail",
        "v1",
        credentials=creds,
    )

    message = MIMEText(body)

    message["To"] = to_email
    message["Subject"] = subject

    raw = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    payload = {
        "raw": raw,
    }

    if thread_id:
        payload["threadId"] = thread_id

    response = (
        service.users()
        .messages()
        .send(
            userId="me",
            body=payload,
        )
        .execute()
    )

    return response
