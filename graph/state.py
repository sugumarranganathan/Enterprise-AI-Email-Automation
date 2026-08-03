"""
====================================================
Shared LangGraph State

Enterprise AI Email Automation

Shared workflow state used by every agent.

Supports:
- Google Colab
- Render
- Local Development
====================================================
"""

from typing import Any, Dict, List, Optional, TypedDict


class EmailState(TypedDict, total=False):

    # ==================================================
    # Original Email
    # ==================================================

    email: str
    sender: str
    subject: str

    thread_id: str
    message_id: str

    # ==================================================
    # Reader Agent
    # ==================================================

    summary: str
    intent: str
    action_items: str

    # ==================================================
    # Classification Agent
    # ==================================================

    category: str
    priority: str
    sentiment: str

    # ==================================================
    # Knowledge Agent (RAG)
    # ==================================================

    knowledge: str
    retrieved_context: str
    knowledge_docs: List[Any]

    # ==================================================
    # Policy Agent
    # ==================================================

    policy: str
    policy_result: str

    # ==================================================
    # Response Generation
    # ==================================================

    draft_reply: str
    response: str

    reviewed_reply: str

    final_email: str

    # ==================================================
    # Approval Agent
    # ==================================================

    approval_status: str

    approval_reason: str

    approval_time: str

    auto_send: bool

    approved: bool

    # ==================================================
    # Email Sender
    # ==================================================

    send_status: str

    send_error: Optional[str]

    sent_time: Optional[str]

    email_sent: bool

    # ==================================================
    # Gmail Response
    # ==================================================

    message_id: Optional[str]

    thread_id: Optional[str]

    # ==================================================
    # History Logger
    # ==================================================

    history: Dict[str, Any]

    # ==================================================
    # Metadata
    # ==================================================

    workflow_status: str

    processing_time: float

    created_at: str

    updated_at: str
