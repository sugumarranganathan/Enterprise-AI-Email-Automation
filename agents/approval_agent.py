"""
Human Approval Agent
"""

from utils.logger import logger


def approval_agent(state):

    logger.info("Approval Agent Started")

    """
    Later this will connect to

    Gradio

    FastAPI

    Dashboard

    Human Click

    Approve / Reject
    """

    state["approval_status"] = "Approved"

    return state
