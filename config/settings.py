"""
====================================================
Enterprise AI Email Automation
Application Settings
====================================================
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    # =====================================================
    # Project
    # =====================================================

    PROJECT_NAME = "Enterprise AI Email Automation"

    VERSION = "1.0.0"

    DEBUG = True

    # =====================================================
    # Groq
    # =====================================================

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    LLM_MODEL = "llama-3.3-70b-versatile"

    TEMPERATURE = 0.2

    MAX_TOKENS = 1024

    # =====================================================
    # Qdrant
    # =====================================================

    QDRANT_URL = os.getenv("QDRANT_URL")

    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

    QDRANT_COLLECTION = "email_knowledge"

    TOP_K = 3

    # =====================================================
    # Embedding Model
    # =====================================================

    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    # =====================================================
    # Gmail
    # =====================================================

    GMAIL_CREDENTIALS = "credentials.json"

    GMAIL_TOKEN = "token.json"

    GMAIL_SCOPES = [
        "https://www.googleapis.com/auth/gmail.send",
        "https://www.googleapis.com/auth/gmail.readonly"
    ]

    # =====================================================
    # Email
    # =====================================================

    DEFAULT_SENDER = "customer@example.com"

    COMPANY_NAME = "Enterprise AI"

    SUPPORT_EMAIL = "contact.sugumarai@gmail.com"

    # =====================================================
    # Workflow
    # =====================================================

    AUTO_SEND = False

    REQUIRE_APPROVAL = True

    SAVE_HISTORY = True

    # =====================================================
    # Logging
    # =====================================================

    LOG_LEVEL = "INFO"

    LOG_FILE = "logs/app.log"

    # =====================================================
    # Gradio
    # =====================================================

    SERVER_NAME = "0.0.0.0"

    SERVER_PORT = 7860

    SHARE = True


settings = Settings()
