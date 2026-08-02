"""
Application Logger

Used by all agents and workflow modules.
"""

import logging
import sys

# =====================================================
# Configure Logging
# =====================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ],
    force=True
)

# =====================================================
# Global Logger
# =====================================================

logger = logging.getLogger("EnterpriseAI")

logger.setLevel(logging.INFO)

# =====================================================
# Test
# =====================================================

if __name__ == "__main__":
    logger.info("Logger initialized successfully.")
