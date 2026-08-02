"""
Index Company Documents

Run only when:
- New PDF added
- PDF updated
- New knowledge base created
"""

import os
import sys
from pathlib import Path

# =====================================================
# Add Project Root to Python Path
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

os.chdir(PROJECT_ROOT)

# =====================================================
# Imports
# =====================================================

from rag.loader import load_documents
from rag.chunker import split_documents
from rag.embeddings import embeddings

from langchain_qdrant import QdrantVectorStore

from tools.qdrant_tool import client
from utils.config import settings

# =====================================================
# Load Documents
# =====================================================

print("=" * 60)
print("Loading PDF documents...")
print("=" * 60)

documents = load_documents()

print(f"✅ Loaded {len(documents)} document(s)")

# =====================================================
# Split Documents
# =====================================================

print("=" * 60)
print("Splitting into chunks...")
print("=" * 60)

chunks = split_documents(documents)

print(f"✅ Created {len(chunks)} chunk(s)")

# =====================================================
# Check Collection
# =====================================================

print("=" * 60)
print("Checking Qdrant Collection...")
print("=" * 60)

if not client.collection_exists(settings.QDRANT_COLLECTION):
    raise Exception(
        f"Collection '{settings.QDRANT_COLLECTION}' does not exist."
    )

print(f"✅ Collection Found : {settings.QDRANT_COLLECTION}")

# =====================================================
# Connect to Existing Collection
# =====================================================

print("=" * 60)
print("Connecting to Qdrant...")
print("=" * 60)

vectorstore = QdrantVectorStore(
    client=client,
    collection_name=settings.QDRANT_COLLECTION,
    embedding=embeddings,
)

# =====================================================
# Upload Documents
# =====================================================

print("=" * 60)
print("Uploading embeddings...")
print("=" * 60)

ids = vectorstore.add_documents(chunks)

print("=" * 60)
print("🎉 Indexing Completed Successfully!")
print("=" * 60)

print(f"Collection : {settings.QDRANT_COLLECTION}")
print(f"Documents  : {len(documents)}")
print(f"Chunks     : {len(chunks)}")
print(f"Uploaded   : {len(ids)} vectors")

info = client.get_collection(settings.QDRANT_COLLECTION)

print()
print("Collection Statistics")
print("-" * 60)
print(f"Points          : {info.points_count}")
print(f"Indexed Vectors : {info.indexed_vectors_count}")
print(f"Status          : {info.status}")

print("=" * 60)
