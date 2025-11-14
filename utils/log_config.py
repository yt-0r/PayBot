import logging
import os
from logging.handlers import RotatingFileHandler

from config import settings

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name: str, log_file: str):

    log_path = os.path.join(LOG_DIR, log_file)

    handler = RotatingFileHandler(
        log_path, maxBytes=5_000_000, backupCount=5, encoding="utf-8"
    )
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(settings.LOG_LEVEL)
    logger.addHandler(handler)
    logger.propagate = False

    return logger


bot_logger = setup_logger("bot", "bot.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s",
)

