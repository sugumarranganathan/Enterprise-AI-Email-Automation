"""
====================================================
Enterprise AI Email Automation
Graph Package
====================================================
"""

from .state import EmailState
from .workflow import graph

__all__ = [
    "EmailState",
    "graph",
]
