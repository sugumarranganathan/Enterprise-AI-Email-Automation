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
    Load Gmail OAuth credentials from Render
    Environment Variables.

    Required Environment Variables
    ------------------------------
    GOOGLE_CLIENT_ID
    GOOGLE_CLIENT_SECRET
    GOOGLE_REFRESH_TOKEN

    Access tokens are automatically refreshed.
    """

    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
    refresh_token = os.getenv("GOOGLE_REFRESH_TOKEN")

    if not client_id:
        raise RuntimeError(
            "GOOGLE_CLIENT_ID environment variable not found."
        )

    if not client_secret:
        raise RuntimeError(
            "GOOGLE_CLIENT_SECRET environment variable not found."
        )

    if not refresh_token:
        raise RuntimeError(
            "GOOGLE_REFRESH_TOKEN environment variable not found."
        )

    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=SCOPES,
    )

    # -----------------------------------------------------
    # Refresh Access Token
    # -----------------------------------------------------

    creds.refresh(Request())

    if not creds.valid:
        raise RuntimeError(
            "Failed to refresh Gmail access token."
        )

    return creds
