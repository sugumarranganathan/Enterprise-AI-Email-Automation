"""
Human Approval Agent

Determine whether an email can be sent automatically
or requires human approval.
"""

from utils.logger import logger


def approval_agent(state):

    logger.info("===== Approval Agent Started =====")

    priority = state.get("priority", "Medium")
    sentiment = state.get("sentiment", "Neutral")
    intent = state.get("intent", "").lower()

    approval_status = "Approved"
    auto_send = True
    reason = "Approved for automatic sending."

    # High priority emails
    if priority.lower() == "high":
        approval_status = "Pending Human Approval"
        auto_send = False
        reason = "High priority email."

    # Negative customer sentiment
    elif sentiment.lower() == "negative":
        approval_status = "Pending Human Approval"
        auto_send = False
        reason = "Negative customer sentiment."

    # Sensitive requests
    elif any(keyword in intent for keyword in [
        "refund",
        "complaint",
        "legal",
        "lawsuit",
        "escalation",
        "compensation"
    ]):
        approval_status = "Pending Human Approval"
        auto_send = False
        reason = "Sensitive customer request."

    state["approval_status"] = approval_status
    state["auto_send"] = auto_send
    state["approval_reason"] = reason

    logger.info(f"Approval Status : {approval_status}")
    logger.info(f"Auto Send       : {auto_send}")
    logger.info(f"Reason          : {reason}")

    logger.info("===== Approval Agent Completed =====")

    return state
