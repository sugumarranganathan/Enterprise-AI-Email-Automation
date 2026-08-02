"""
Human Approval Agent

Determine whether an email can be sent automatically
or requires human approval.
"""

from datetime import datetime

from utils.logger import logger


def approval_agent(state):

    logger.info("===== Approval Agent Started =====")

    # -------------------------------------------------
    # Read previous agent outputs
    # -------------------------------------------------

    priority = str(state.get("priority", "Medium")).strip()
    sentiment = str(state.get("sentiment", "Neutral")).strip()
    intent = str(state.get("intent", "")).strip().lower()

    logger.info(f"Priority  : {priority}")
    logger.info(f"Sentiment : {sentiment}")
    logger.info(f"Intent    : {intent}")

    # -------------------------------------------------
    # Default Decision
    # -------------------------------------------------

    approval_status = "Approved"
    auto_send = True
    approval_reason = "Approved for automatic sending."

    # -------------------------------------------------
    # Approval Rules
    # -------------------------------------------------

    if priority.lower() == "high":

        approval_status = "Pending Human Approval"
        auto_send = False
        approval_reason = "High priority email."

    elif sentiment.lower() == "negative":

        approval_status = "Pending Human Approval"
        auto_send = False
        approval_reason = "Negative customer sentiment."

    elif any(
        keyword in intent
        for keyword in [
            "refund",
            "complaint",
            "legal",
            "lawsuit",
            "escalation",
            "compensation",
            "chargeback",
            "fraud",
        ]
    ):

        approval_status = "Pending Human Approval"
        auto_send = False
        approval_reason = "Sensitive customer request."

    # -------------------------------------------------
    # Store Results
    # -------------------------------------------------

    state["approval_status"] = approval_status
    state["auto_send"] = auto_send
    state["approval_reason"] = approval_reason
    state["approval_time"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # -------------------------------------------------
    # Logging
    # -------------------------------------------------

    logger.info(f"Approval Status : {approval_status}")
    logger.info(f"Auto Send       : {auto_send}")
    logger.info(f"Reason          : {approval_reason}")
    logger.info("===== Approval Agent Completed =====")

    return state
