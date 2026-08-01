"""
Enterprise AI Email Automation

LangGraph Workflow
"""

from langgraph.graph import StateGraph
from langgraph.graph import END

from graph.state import EmailState

from agents.email_listener import email_listener
from agents.classification_agent import classification_agent
from agents.priority_agent import priority_agent
from agents.sentiment_agent import sentiment_agent
from agents.reader_agent import reader_agent
from agents.knowledge_agent import knowledge_agent
from agents.policy_agent import policy_agent
from agents.responder_agent import responder_agent
from agents.reviewer_agent import reviewer_agent
from agents.formatter_agent import formatter_agent
from agents.approval_agent import approval_agent
from agents.email_sender import email_sender
from agents.history_logger import history_logger


workflow = StateGraph(EmailState)


# --------------------------------------------------
# Register Nodes
# --------------------------------------------------

workflow.add_node("listener", email_listener)

workflow.add_node("classification", classification_agent)

workflow.add_node("priority", priority_agent)

workflow.add_node("sentiment", sentiment_agent)

workflow.add_node("reader", reader_agent)

workflow.add_node("knowledge", knowledge_agent)

workflow.add_node("policy", policy_agent)

workflow.add_node("responder", responder_agent)

workflow.add_node("reviewer", reviewer_agent)

workflow.add_node("formatter", formatter_agent)

workflow.add_node("approval", approval_agent)

workflow.add_node("sender", email_sender)

workflow.add_node("history", history_logger)


# --------------------------------------------------
# Entry Point
# --------------------------------------------------

workflow.set_entry_point("listener")


# --------------------------------------------------
# Workflow
# --------------------------------------------------

workflow.add_edge("listener", "classification")

workflow.add_edge("classification", "priority")

workflow.add_edge("priority", "sentiment")

workflow.add_edge("sentiment", "reader")

workflow.add_edge("reader", "knowledge")

workflow.add_edge("knowledge", "policy")

workflow.add_edge("policy", "responder")

workflow.add_edge("responder", "reviewer")

workflow.add_edge("reviewer", "formatter")

workflow.add_edge("formatter", "approval")

workflow.add_edge("approval", "sender")

workflow.add_edge("sender", "history")

workflow.add_edge("history", END)


graph = workflow.compile()
