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
# Create Qdrant Client
# =====================================================

client = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY,
    prefer_grpc=False,
    timeout=60,
    check_compatibility=False,
)


# =====================================================
# Test Connection
# =====================================================

def test_connection():
    """
    Verify Qdrant Cloud connection.
    """

    try:

        collections = client.get_collections()

        print("✅ Connected to Qdrant Cloud")

        print(
            "Collections :",
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
