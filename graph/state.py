"""
Shared LangGraph State

Every agent reads from and writes to this state.
"""

from typing import TypedDict


class EmailState(TypedDict, total=False):

    # --------------------------------------------------
    # Email
    # --------------------------------------------------

    email: str
    sender: str
    subject: str

    thread_id: str
    message_id: str

    # --------------------------------------------------
    # Reader Agent
    # --------------------------------------------------

    summary: str
    intent: str
    action_items: str

    # --------------------------------------------------
    # Classification
    # --------------------------------------------------

    category: str
    priority: str
    sentiment: str

    # --------------------------------------------------
    # Knowledge (RAG)
    # --------------------------------------------------

    knowledge: str
    retrieved_context: str
    knowledge_docs: list

    # --------------------------------------------------
    # Policy
    # --------------------------------------------------

    policy: str
    policy_result: str

    # --------------------------------------------------
    # Response
    # --------------------------------------------------

    draft_reply: str
    reviewed_reply: str
    final_email: str

    # --------------------------------------------------
    # Approval
    # --------------------------------------------------

    approval_status: str
    approval_reason: str
    auto_send: bool

    # --------------------------------------------------
    # Email Sender
    # --------------------------------------------------

    send_status: str
    send_error: str
    sent_time: str

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    history: dict
