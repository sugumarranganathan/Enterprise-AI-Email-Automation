"""
Read Latest Gmail Message
"""

import base64

from googleapiclient.discovery import build

from tools.gmail_auth import get_gmail_credentials


def read_latest_email():

    creds = get_gmail_credentials()

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    results = service.users().messages().list(
        userId="me",
        maxResults=1,
        labelIds=["INBOX"]
    ).execute()

    messages = results.get("messages", [])

    if not messages:
        return None

    message = service.users().messages().get(
        userId="me",
        id=messages[0]["id"],
        format="full"
    ).execute()

    headers = message["payload"]["headers"]

    subject = ""
    sender = ""

    for h in headers:

        if h["name"] == "Subject":
            subject = h["value"]

        elif h["name"] == "From":
            sender = h["value"]

    body = ""

    payload = message["payload"]

    if "parts" in payload:

        for part in payload["parts"]:

            if part.get("mimeType") == "text/plain":

                data = part["body"].get("data")

                if data:

                    body = base64.urlsafe_b64decode(
                        data
                    ).decode()

                break

    elif "body" in payload and "data" in payload["body"]:

        body = base64.urlsafe_b64decode(
            payload["body"]["data"]
        ).decode()

    return {

        "sender": sender,

        "subject": subject,

        "email": body,

        "thread_id": message.get("threadId"),

        "message_id": message.get("id")

    }
