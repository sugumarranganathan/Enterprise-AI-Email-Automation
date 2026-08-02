"""
Enterprise AI Logger
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
