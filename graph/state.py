"""
Shared LangGraph State

Every agent reads from and writes to this state.
"""

from typing import TypedDict


class EmailState(TypedDict):

    # Raw email
    email: str

    # Email metadata
    sender: str
    subject: str
    send_status: str
    thread_id: str
    message_id: str

    # Classification
    category: str
    priority: str
    sentiment: str

    # Reader Agent
    summary: str
    intent: str
    action_items: str

    # RAG
    retrieved_context: str

    # Policy Agent
    policy_result: str

    # Response
    draft_reply: str

    # Reviewer
    reviewed_reply: str

    # Formatter
    final_email: str

    # Approval
    approval_status: str

    # Send status
    send_status: str
