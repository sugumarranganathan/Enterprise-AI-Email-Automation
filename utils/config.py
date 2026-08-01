"""
Application Configuration

Supports:
- Google Colab Secrets
- Local .env
- Render Environment Variables
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------
# Detect Google Colab
# ---------------------------------------------------------

try:
    from google.colab import userdata
    IS_COLAB = True
except ImportError:
    IS_COLAB = False


def get_secret(name, default=None):
    """
    Read secret from:
    1. Google Colab Secrets
    2. Environment Variables
    3. Default value
    """

    if IS_COLAB:
        try:
            value = userdata.get(name)
            if value:
                return value
        except Exception:
            pass

    return os.getenv(name, default)


class Settings:

    # -----------------------------
    # API Keys
    # -----------------------------

    GROQ_API_KEY = get_secret("GROQ_API_KEY")

    # Support both names
    QDRANT_URL = (
        get_secret("QDRANT_URL")
        or get_secret("QDRANT_UR")
    )

    QDRANT_API_KEY = get_secret("QDRANT_API_KEY")

    # -----------------------------
    # Qdrant
    # -----------------------------

    QDRANT_COLLECTION = get_secret(
        "QDRANT_COLLECTION",
        "email_knowledge"
    )

    # -----------------------------
    # Database
    # -----------------------------

    DATABASE_URL = get_secret(
        "DATABASE_URL",
        "sqlite:///database/email_history.db"
    )


settings = Settings()
