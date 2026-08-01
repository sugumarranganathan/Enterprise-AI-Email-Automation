"""
Application Configuration

Works in:

✅ Google Colab
✅ Local Linux
✅ Render
"""

import os

from dotenv import load_dotenv

load_dotenv()

# ----------------------------------------------------
# Detect Google Colab
# ----------------------------------------------------

try:
    from google.colab import userdata

    IS_COLAB = True

except ImportError:
    IS_COLAB = False


class Settings:

    if IS_COLAB:

        GROQ_API_KEY = userdata.get("GROQ_API_KEY")

        QDRANT_URL = userdata.get("QDRANT_URL")

        QDRANT_API_KEY = userdata.get("QDRANT_API_KEY")

    else:

        GROQ_API_KEY = os.getenv("GROQ_API_KEY")

        QDRANT_URL = os.getenv("QDRANT_URL")

        QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

    QDRANT_COLLECTION = os.getenv(
        "QDRANT_COLLECTION",
        "email_knowledge"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///database/email_history.db"
    )


settings = Settings()
