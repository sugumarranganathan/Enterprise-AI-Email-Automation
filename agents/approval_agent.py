"""
====================================================
Approval Agent

Determines whether an email should be sent
automatically or requires human approval.

Supports:
- Google Colab
- Render
- Local Development
====================================================
"""

from datetime import datetime

from utils.logger import logger


# =====================================================
# Approval Agent
# =====================================================

def approval_agent(state):

    logger.info("=" * 60)
    logger.info("Approval Agent Started")
    logger.info("=" * 60)

    # =====================================================
    # Read Workflow State
    # =====================================================

    priority = str(
        state.get("priority", "Medium")
    ).strip()

    sentiment = str(
        state.get("sentiment", "Neutral")
    ).strip()

    intent = str(
        state.get("intent", "")
    ).lower().strip()

    category = str(
        state.get("category", "")
    ).lower().strip()

    logger.info(f"Priority  : {priority}")
    logger.info(f"Sentiment : {sentiment}")
    logger.info(f"Category  : {category}")
    logger.info(f"Intent    : {intent}")

    # =====================================================
    # Default Decision
    # =====================================================

    approval_status = "Approved"

    auto_send = True

    approval_reason = "Safe for automatic email delivery."

    # =====================================================
    # Approval Rules
    # =====================================================

    HIGH_RISK_KEYWORDS = [

        "refund",

        "chargeback",

        "legal",

        "lawsuit",

        "fraud",

        "compensation",

        "escalation",

        "consumer court",

        "police",

        "cyber crime",

        "cancel order",

        "cancel subscription",

        "complaint",

        "replacement",

        "return"

    ]

    # High Priority
    if priority.lower() == "high":

        approval_status = "Pending Human Approval"

        auto_send = False

        approval_reason = "High priority customer request."

    # Negative Sentiment
    elif sentiment.lower() == "negative":

        approval_status = "Pending Human Approval"

        auto_send = False

        approval_reason = "Negative customer sentiment detected."

    # Sensitive Category
    elif category in [

        "legal",

        "finance",

        "complaint"

    ]:

        approval_status = "Pending Human Approval"

        auto_send = False

        approval_reason = "Sensitive email category."

    # Sensitive Intent
    elif any(

        keyword in intent

        for keyword in HIGH_RISK_KEYWORDS

    ):

        approval_status = "Pending Human Approval"

        auto_send = False

        approval_reason = "Sensitive customer request."

    # =====================================================
    # Save Workflow State
    # =====================================================

    state["approval_status"] = approval_status

    state["auto_send"] = auto_send

    state["approval_reason"] = approval_reason

    state["approval_time"] = datetime.now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )

    # Compatibility

    state["approved"] = auto_send

    # =====================================================
    # Logging
    # =====================================================

    logger.info(f"Approval Status : {approval_status}")
    logger.info(f"Auto Send       : {auto_send}")
    logger.info(f"Reason          : {approval_reason}")

    logger.info("=" * 60)
    logger.info("Approval Agent Completed")
    logger.info("=" * 60)

    return state
