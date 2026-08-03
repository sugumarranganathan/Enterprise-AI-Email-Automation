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

# =====================================================
# Load .env
# =====================================================

load_dotenv()

# =====================================================
# Detect Google Colab
# =====================================================

try:
    from google.colab import userdata
    IS_COLAB = True
except ImportError:
    IS_COLAB = False


# =====================================================
# Secret Loader
# =====================================================

def get_secret(name: str, default=None):
    """
    Read configuration in the following order:

    1. Google Colab Secrets
    2. Environment Variables
    3. Default Value
    """

    # ------------------------
    # Google Colab
    # ------------------------

    if IS_COLAB:
        try:
            value = userdata.get(name)

            if value and str(value).strip():
                return str(value).strip()

        except Exception:
            pass

    # ------------------------
    # Environment Variables
    # ------------------------

    value = os.getenv(name)

    if value and str(value).strip():
        return str(value).strip()

    return default


# =====================================================
# Settings
# =====================================================

class Settings:

    def __init__(self):

        # =================================================
        # API Keys
        # =================================================

        self.GROQ_API_KEY = get_secret("GROQ_API_KEY")

        self.QDRANT_URL = get_secret("QDRANT_URL")

        self.QDRANT_API_KEY = get_secret("QDRANT_API_KEY")

        # =================================================
        # Qdrant
        # =================================================

        self.QDRANT_COLLECTION = get_secret(
            "QDRANT_COLLECTION",
            "email_knowledge"
        )

        # =================================================
        # Database
        # =================================================

        self.DATABASE_URL = get_secret(
            "DATABASE_URL",
            "sqlite:///database/email_history.db"
        )

        # =================================================
        # Export to Environment
        # =================================================

        if self.GROQ_API_KEY:
            os.environ["GROQ_API_KEY"] = self.GROQ_API_KEY

        if self.QDRANT_URL:
            os.environ["QDRANT_URL"] = self.QDRANT_URL

        if self.QDRANT_API_KEY:
            os.environ["QDRANT_API_KEY"] = self.QDRANT_API_KEY

    # =================================================
    # Validation
    # =================================================

    def validate(self):

        missing = []

        if not self.GROQ_API_KEY:
            missing.append("GROQ_API_KEY")

        if not self.QDRANT_URL:
            missing.append("QDRANT_UR")

        if not self.QDRANT_API_KEY:
            missing.append("QDRANT_API_KEY")

        if missing:

            raise ValueError(

                "Missing configuration: "

                + ", ".join(missing)

            )


# =====================================================
# Global Settings
# =====================================================

settings = Settings()
