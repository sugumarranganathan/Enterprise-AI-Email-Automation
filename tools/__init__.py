"""
====================================================
Enterprise AI Email Automation
Tools Package
====================================================
"""

from .gmail_reader import read_emails
from .gmail_sender import send_email
from .qdrant_tool import client

__all__ = [
    "read_emails",
    "send_email",
    "client",
]
