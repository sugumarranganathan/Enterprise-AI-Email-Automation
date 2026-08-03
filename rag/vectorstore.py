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
    raise ValueError("QDRANT_URL is missing.")

if not settings.QDRANT_API_KEY:
    raise ValueError("QDRANT_API_KEY is missing.")


# =====================================================
# Qdrant Client
# =====================================================

client = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY,
    prefer_grpc=False,
    check_compatibility=False,
    timeout=60,
)


# =====================================================
# Test Connection
# =====================================================

try:

    collections = client.get_collections()

    print("✅ Connected to Qdrant Cloud")
    print("Collections:", [c.name for c in collections.collections])

except Exception as e:

    print("❌ Failed to connect to Qdrant Cloud")
    raise e
