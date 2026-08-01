from tools.gmail_reader import read_latest_email

from utils.logger import logger


def email_listener(state):

    logger.info("Reading Gmail...")

    email = read_latest_email()

    if email:

        state["sender"] = email["sender"]

        state["subject"] = email["subject"]

        state["email"] = email["email"]

        state["thread_id"] = email["thread_id"]

        state["message_id"] = email["message_id"]

    return state
