"""
====================================================
History Logger Agent

Stores workflow execution details
for auditing and debugging.

Supports:
- Google Colab
- Render
- Local Development
====================================================
"""

from datetime import datetime

from utils.logger import logger


# =====================================================
# History Logger
# =====================================================

def history_logger(state):

    logger.info("=" * 60)
    logger.info("History Logger Started")
    logger.info("=" * 60)

    try:

        history = {

            # ============================================
            # Timestamp
            # ============================================

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            # ============================================
            # Email
            # ============================================

            "sender": state.get("sender"),

            "subject": state.get("subject"),

            "thread_id": state.get("thread_id"),

            "message_id": state.get("message_id"),

            # ============================================
            # Reader
            # ============================================

            "summary": state.get("summary"),

            "intent": state.get("intent"),

            # ============================================
            # Classification
            # ============================================

            "category": state.get("category"),

            "priority": state.get("priority"),

            "sentiment": state.get("sentiment"),

            # ============================================
            # Knowledge
            # ============================================

            "knowledge": state.get("knowledge"),

            # ============================================
            # Policy
            # ============================================

            "policy": state.get("policy_result"),

            # ============================================
            # Response
            # ============================================

            "draft_reply": state.get("draft_reply"),

            "reviewed_reply": state.get("reviewed_reply"),

            "final_email": state.get("final_email"),

            # ============================================
            # Approval
            # ============================================

            "approval_status": state.get("approval_status"),

            "approval_reason": state.get("approval_reason"),

            "approval_time": state.get("approval_time"),

            "auto_send": state.get("auto_send"),

            # ============================================
            # Sender
            # ============================================

            "send_status": state.get("send_status"),

            "send_error": state.get("send_error"),

            "sent_time": state.get("sent_time"),

            "email_sent": state.get("email_sent"),

        }

        # ================================================
        # Save History
        # ================================================

        state["history"] = history

        logger.info("Workflow history recorded successfully.")

        logger.info(
            f"Status : {history['send_status']}"
        )

        logger.info(
            f"Approval : {history['approval_status']}"
        )

    except Exception as e:

        logger.exception(
            "History Logger Failed"
        )

        state["history"] = {}

        state["history_error"] = str(e)

    logger.info("=" * 60)
    logger.info("History Logger Completed")
    logger.info("=" * 60)

    return state
