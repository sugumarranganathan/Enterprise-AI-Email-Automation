"""
History Logger Agent

Stores workflow results for auditing.
"""

from datetime import datetime

from utils.logger import logger


def history_logger(state):

    logger.info("=" * 60)
    logger.info("===== History Logger Started =====")
    logger.info("=" * 60)

    try:

        history = {

            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "sender": state.get("sender"),

            "subject": state.get("subject"),

            "summary": state.get("summary"),

            "intent": state.get("intent"),

            "priority": state.get("priority"),

            "sentiment": state.get("sentiment"),

            "approval_status": state.get("approval_status"),

            "send_status": state.get("send_status"),

            "message_id": state.get("message_id"),

            "thread_id": state.get("thread_id"),

        }

        state["history"] = history

        logger.info("History record created successfully.")
        logger.info(history)

    except Exception as e:

        logger.exception("History Logger Failed")

        state["history"] = None
        state["history_error"] = str(e)

    logger.info("=" * 60)
    logger.info("===== History Logger Completed =====")
    logger.info("=" * 60)

    return state
