"""
====================================================
Enterprise AI Email Automation
Reusable UI Components
====================================================
"""

import gradio as gr


# =====================================================
# Dashboard Card
# =====================================================

def dashboard_card(title: str, value: str, emoji: str = "📌"):

    value = value if value else "-"

    return gr.Markdown(
        f"""
### {emoji} {title}

**{value}**
"""
    )


# =====================================================
# Status Badge
# =====================================================

def status_badge(text: str):

    return gr.Markdown(
        f"""
### ✅ {text}
"""
    )


# =====================================================
# Section Title
# =====================================================

def section(title: str):

    return gr.Markdown(f"## {title}")


# =====================================================
# Horizontal Divider
# =====================================================

def divider():

    return gr.Markdown("---")


# =====================================================
# Read Only Textbox
# =====================================================

def readonly_textbox(label, lines=1):

    return gr.Textbox(
        label=label,
        lines=lines,
        interactive=False
    )


# =====================================================
# Large Read Only Textbox
# =====================================================

def readonly_large(label, lines=10):

    return gr.Textbox(
        label=label,
        lines=lines,
        interactive=False
    )


# =====================================================
# Primary Button
# =====================================================

def primary_button(text):

    return gr.Button(
        text,
        variant="primary"
    )


# =====================================================
# Secondary Button
# =====================================================

def secondary_button(text):

    return gr.Button(text)


# =====================================================
# Approval Buttons
# =====================================================

def approval_buttons():

    approve = gr.Button(
        "✅ Approve",
        variant="primary"
    )

    reject = gr.Button(
        "❌ Reject",
        variant="stop"
    )

    return approve, reject
