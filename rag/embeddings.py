"""
====================================================
Embeddings

Supports:
- Google Colab
- Render
- Local Development
====================================================
"""

from langchain_huggingface import HuggingFaceEmbeddings


# =====================================================
# Embedding Model
# =====================================================

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


# =====================================================
# HuggingFace Embeddings
# =====================================================

embeddings = HuggingFaceEmbeddings(

    model_name=MODEL_NAME,

    model_kwargs={

        "device": "cpu"

    },

    encode_kwargs={

        "normalize_embeddings": True

    }

)


# =====================================================
# Manual Test
# =====================================================

if __name__ == "__main__":

    print("✅ Embedding Model Loaded")
    print("Model :", MODEL_NAME)

    vector = embeddings.embed_query("Hello World")

    print("Embedding Dimension :", len(vector))
