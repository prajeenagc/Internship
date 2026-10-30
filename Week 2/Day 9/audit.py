import logging

logger = logging.getLogger(__name__)


def record_audit(action: str):
    logger.info("AUDIT: %s", action)