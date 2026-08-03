"""
====================================================
Gmail OAuth Authentication
Render Production Version

Author : Sugumar R
====================================================
"""

import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# =====================================================
# Gmail Scopes
# =====================================================

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]

# =====================================================
# Gmail Credentials
# =====================================================

def get_gmail_credentials():
    """
    Load Gmail OAuth credentials.

    Production Flow
    ----------------
    1. Read token.json
    2. Refresh automatically if expired
    3. Never open a browser
    """

    token_file = "token.json"
    credentials_file = "credentials.json"

    # -------------------------------------------------
    # Check Required Files
    # -------------------------------------------------

    if not os.path.exists(credentials_file):
        raise FileNotFoundError(
            "\n"
            "credentials.json not found.\n"
            "Place credentials.json in the project root "
            "before deploying to Render."
        )

    if not os.path.exists(token_file):
        raise FileNotFoundError(
            "\n"
            "token.json not found.\n\n"
            "Generate token.json locally first.\n"
            "Then upload it with your project."
        )

    # -------------------------------------------------
    # Load Token
    # -------------------------------------------------

    creds = Credentials.from_authorized_user_file(
        token_file,
        SCOPES,
    )

    # -------------------------------------------------
    # Refresh Token
    # -------------------------------------------------

    if creds.expired and creds.refresh_token:

        creds.refresh(Request())

        with open(token_file, "w") as token:
            token.write(creds.to_json())

    # -------------------------------------------------
    # Validate
    # -------------------------------------------------

    if not creds.valid:
        raise RuntimeError(
            "Invalid Gmail OAuth credentials."
        )

    return creds
