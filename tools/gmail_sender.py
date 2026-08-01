import base64

from email.mime.text import MIMEText

from googleapiclient.discovery import build

from tools.gmail_auth import get_gmail_credentials


def reply_email(

    to_email,

    subject,

    body,

    thread_id

):

    creds = get_gmail_credentials()

    service = build(

        "gmail",

        "v1",

        credentials=creds

    )

    message = MIMEText(body)

    message["to"] = to_email

    message["subject"] = "Re: " + subject

    raw = base64.urlsafe_b64encode(

        message.as_bytes()

    ).decode()

    service.users().messages().send(

        userId="me",

        body={

            "raw": raw,

            "threadId": thread_id

        }

    ).execute()
