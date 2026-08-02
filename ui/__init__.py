"""
====================================================
Enterprise AI Email Automation
UI Package
====================================================

Reusable Gradio UI components.
"""

from .dashboard import create_dashboard
from .components import (
    dashboard_card,
    status_badge,
    section,
    divider,
    readonly_textbox,
    readonly_large,
    primary_button,
    secondary_button,
    approval_buttons,
)

__all__ = [
    "create_dashboard",
    "dashboard_card",
    "status_badge",
    "section",
    "divider",
    "readonly_textbox",
    "readonly_large",
    "primary_button",
    "secondary_button",
    "approval_buttons",
]
