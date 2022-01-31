import os
import sys
from loguru import logger

LOG_FILE = os.environ.get("LOG_FILE")

log_format = "{time} - {name} - {level} - {message}"

if LOG_FILE:
    logger.add(LOG_FILE, format=log_format, serialize=True,
            level="DEBUG", rotation="1 week", compression="zip", colorize=True)

logger.add(sys.stdout, format=log_format, serialize=True, level="DEBUG", colorize=True)
