"""
====================================================
Application Configuration

Supports:
- Google Colab Secrets
- Local .env
- Render Environment Variables
====================================================
"""

import os
from dotenv import load_dotenv

# Load local .env if available
load_dotenv()


# ====================================================
# Detect Google Colab
# ====================================================

try:
    from google.colab import userdata
    IS_COLAB = True
except ImportError:
    IS_COLAB = False


# ====================================================
# Secret Loader
# ====================================================

def get_secret(name: str, default=None):
    """
    Read secrets in this order:

    1. Google Colab Secrets
    2. Environment Variables
    3. Default Value
    """

    if IS_COLAB:
        try:
            value = userdata.get(name)

            if value is not None and str(value).strip() != "":
                return str(value).strip()

        except Exception:
            pass

    value = os.environ.get(name)

    if value is not None and str(value).strip() != "":
        return str(value).strip()

    return default


# ====================================================
# Settings
# ====================================================

class Settings:

    def __init__(self):

        # ----------------------------
        # API Keys
        # ----------------------------

        self.GROQ_API_KEY = get_secret("GROQ_API_KEY")

        self.QDRANT_URL = (
            get_secret("QDRANT_URL")
            or get_secret("QDRANT_UR")
        )

        self.QDRANT_API_KEY = get_secret("QDRANT_API_KEY")

        # ----------------------------
        # Qdrant
        # ----------------------------

        self.QDRANT_COLLECTION = get_secret(
            "QDRANT_COLLECTION",
            "email_knowledge"
        )

        # ----------------------------
        # Database
        # ----------------------------

        self.DATABASE_URL = get_secret(
            "DATABASE_URL",
            "sqlite:///database/email_history.db"
        )


# ====================================================
# Global Settings Object
# ====================================================

settings = Settings()
