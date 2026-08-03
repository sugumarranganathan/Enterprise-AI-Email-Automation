"""
====================================================
Google OAuth Login
Enterprise AI Email Automation

Author : Sugumar R
====================================================
"""

import os
import secrets

from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow

# =====================================================
# Router
# =====================================================

router = APIRouter(tags=["Google OAuth"])

# =====================================================
# Gmail OAuth Scopes
# =====================================================

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]

# =====================================================
# Google Login
# =====================================================

@router.get("/auth/google")
def google_login():
    """
    Redirect user to Google OAuth Login.
    """

    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
    redirect_uri = os.getenv("GOOGLE_REDIRECT_URI")

    if not client_id:
        return {
            "status": "error",
            "message": "GOOGLE_CLIENT_ID not configured."
        }

    if not client_secret:
        return {
            "status": "error",
            "message": "GOOGLE_CLIENT_SECRET not configured."
        }

    if not redirect_uri:
        return {
            "status": "error",
            "message": "GOOGLE_REDIRECT_URI not configured."
        }

    client_config = {
        "web": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
        }
    }

    flow = Flow.from_client_config(
        client_config,
        scopes=SCOPES,
    )

    flow.redirect_uri = redirect_uri

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent",
        state=secrets.token_urlsafe(32),
    )

    return RedirectResponse(url=authorization_url)
