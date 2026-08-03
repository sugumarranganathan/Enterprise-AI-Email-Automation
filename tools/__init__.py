"""
====================================================
Enterprise AI Email Automation
Tools Package
====================================================
"""

from .gmail_reader import read_latest_email
from .gmail_sender import send_email
from .qdrant_tool import client

__all__ = [
    "read_latest_email",
    "send_email",
    "client",
]
