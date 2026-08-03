"""
====================================================
Qdrant Cloud Connection

Supports:
- Google Colab
- Render
- Local Development
====================================================
"""

from qdrant_client import QdrantClient
from utils.config import settings


# =====================================================
# Validate Configuration
# =====================================================

if not settings.QDRANT_URL:
    raise ValueError(
        "QDRANT_URL is missing. Please configure it in Colab Secrets, "
        ".env, or Render Environment Variables."
    )

if not settings.QDRANT_API_KEY:
    raise ValueError(
        "QDRANT_API_KEY is missing. Please configure it in Colab Secrets, "
        ".env, or Render Environment Variables."
    )


# =====================================================
# Create Qdrant Client
# =====================================================

client = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY,
    prefer_grpc=False,
    check_compatibility=False,
    timeout=60,
)


# =====================================================
# Test Connection (Optional)
# =====================================================

def test_connection():
    """
    Test connection to Qdrant Cloud.
    Call this manually for debugging.
    """

    try:
        collections = client.get_collections()

        print("✅ Connected to Qdrant Cloud")
        print(
            "Collections:",
            [c.name for c in collections.collections]
        )

        return True

    except Exception as e:

        print("❌ Qdrant Connection Failed")
        print(e)

        return False


# =====================================================
# Manual Test
# =====================================================

if __name__ == "__main__":
    test_connection()
