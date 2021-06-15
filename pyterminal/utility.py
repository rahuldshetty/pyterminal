import sys
import logging

def init_logger():
    logger = logging.getLogger('pyterminal')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(
        logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
    )
    logger.addHandler(handler)
    return logger

logger = init_logger()