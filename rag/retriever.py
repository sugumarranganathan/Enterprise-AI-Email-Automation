"""
Retriever
"""

from rag.vectorstore import vectorstore


retriever = vectorstore.as_retriever(

    search_kwargs={

        "k": 3

    }

)


def retrieve(question):

    return retriever.invoke(question)
