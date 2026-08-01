"""
Index Company Documents

Run only when

- New PDF added
- PDF updated
- New knowledge base created
"""

from rag.loader import load_documents
from rag.chunker import split_documents
from rag.embeddings import embeddings

from langchain_qdrant import QdrantVectorStore

from tools.qdrant_tool import client

from utils.config import settings


print("Loading PDFs...")

documents = load_documents()

print(f"Loaded {len(documents)} documents")


print("Splitting...")

chunks = split_documents(documents)

print(f"Created {len(chunks)} chunks")


print("Uploading to Qdrant...")


QdrantVectorStore.from_documents(

    documents=chunks,

    embedding=embeddings,

    url=settings.QDRANT_URL,

    api_key=settings.QDRANT_API_KEY,

    collection_name=settings.QDRANT_COLLECTION

)

print("Finished")
