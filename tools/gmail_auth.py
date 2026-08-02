"""
Gmail OAuth Authentication
"""

import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]


def get_gmail_credentials():

    token_file = "token.json"
    credentials_file = "credentials.json"

    creds = None

    # -----------------------------------------------------
    # Load Existing Token
    # -----------------------------------------------------

    if os.path.exists(token_file):

        creds = Credentials.from_authorized_user_file(
            token_file,
            SCOPES
        )

    # -----------------------------------------------------
    # Refresh or Login
    # -----------------------------------------------------

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:

            creds.refresh(Request())

        else:

            if not os.path.exists(credentials_file):

                raise FileNotFoundError(
                    "\n"
                    "credentials.json not found.\n\n"
                    "Download your OAuth Client credentials from\n"
                    "Google Cloud Console and place\n"
                    "credentials.json in the project root folder.\n"
                )

            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file,
                SCOPES
            )

            creds = flow.run_local_server(
                port=0,
                open_browser=True
            )

        # Save Token

        with open(token_file, "w") as token:

            token.write(creds.to_json())

    return creds
