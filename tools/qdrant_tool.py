"""
Qdrant Cloud Connection
"""

from qdrant_client import QdrantClient

from utils.config import settings


client = QdrantClient(

    url=settings.QDRANT_UR,

    api_key=settings.QDRANT_API_KEY

)
