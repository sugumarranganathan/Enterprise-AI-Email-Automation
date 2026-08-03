"""
Shared Groq Client
"""

import os

from utils.config import settings
from langchain_groq import ChatGroq

# Export the API key to the environment
if settings.GROQ_API_KEY:
    os.environ["GROQ_API_KEY"] = settings.GROQ_API_KEY
else:
    raise ValueError("GROQ_API_KEY not found.")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
    max_tokens=2048,
)
