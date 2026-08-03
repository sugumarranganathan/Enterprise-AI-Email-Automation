"""
====================================================
LangGraph Workflow

Enterprise AI Email Automation

Supports:
- Google Colab
- Render
- Local Development
====================================================
"""

from langgraph.graph import StateGraph, END

from graph.state import EmailState

# =====================================================
# Import Agents
# =====================================================

from agents.reader_agent import reader_agent
from agents.classification_agent import classification_agent
from agents.priority_agent import priority_agent
from agents.sentiment_agent import sentiment_agent
from agents.knowledge_agent import knowledge_agent
from agents.policy_agent import policy_agent
from agents.responder_agent import responder_agent
from agents.reviewer_agent import reviewer_agent
from agents.formatter_agent import formatter_agent
from agents.approval_agent import approval_agent
from agents.email_sender import email_sender
from agents.history_logger import history_logger


# =====================================================
# Create Workflow
# =====================================================

workflow = StateGraph(EmailState)


# =====================================================
# Register Nodes
# =====================================================

workflow.add_node("reader", reader_agent)

workflow.add_node("classification", classification_agent)

workflow.add_node("priority", priority_agent)

workflow.add_node("sentiment", sentiment_agent)

workflow.add_node("knowledge", knowledge_agent)

workflow.add_node("policy", policy_agent)

workflow.add_node("responder", responder_agent)

workflow.add_node("reviewer", reviewer_agent)

workflow.add_node("formatter", formatter_agent)

workflow.add_node("approval", approval_agent)

workflow.add_node("sender", email_sender)

workflow.add_node("history", history_logger)


# =====================================================
# Entry Point
# =====================================================

workflow.set_entry_point("reader")


# =====================================================
# Workflow Pipeline
# =====================================================

workflow.add_edge(
    "reader",
    "classification"
)

workflow.add_edge(
    "classification",
    "priority"
)

workflow.add_edge(
    "priority",
    "sentiment"
)

workflow.add_edge(
    "sentiment",
    "knowledge"
)

workflow.add_edge(
    "knowledge",
    "policy"
)

workflow.add_edge(
    "policy",
    "responder"
)

workflow.add_edge(
    "responder",
    "reviewer"
)

workflow.add_edge(
    "reviewer",
    "formatter"
)

workflow.add_edge(
    "formatter",
    "approval"
)

workflow.add_edge(
    "approval",
    "sender"
)

workflow.add_edge(
    "sender",
    "history"
)

workflow.add_edge(
    "history",
    END
)


# =====================================================
# Compile Graph
# =====================================================

graph = workflow.compile()


# =====================================================
# Manual Test
# =====================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Enterprise AI Email Automation")
    print("LangGraph Workflow")
    print("=" * 60)

    print("Workflow compiled successfully.")

    print()

    print("Pipeline")

    print("Reader")

    print(" ↓")

    print("Classification")

    print(" ↓")

    print("Priority")

    print(" ↓")

    print("Sentiment")

    print(" ↓")

    print("Knowledge (Qdrant)")

    print(" ↓")

    print("Policy")

    print(" ↓")

    print("Responder")

    print(" ↓")

    print("Reviewer")

    print(" ↓")

    print("Formatter")

    print(" ↓")

    print("Approval")

    print(" ↓")

    print("Email Sender")

    print(" ↓")

    print("History Logger")

    print()

    print("Workflow Ready.")
