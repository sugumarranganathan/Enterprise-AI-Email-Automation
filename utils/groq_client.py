"""
Shared Groq Client
"""

from langchain_groq import ChatGroq

from utils.config import settings


llm = ChatGroq(

    groq_api_key=settings.GROQ_API_KEY,

    model="llama-3.3-70b-versatile",

    temperature=0.2,

    max_tokens=2048
)
