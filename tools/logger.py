import os
import sys
import logging
from logging.handlers import RotatingFileHandler


LOG_DIR = "logs"
LOG_FILENAME = "running_logs.log"
LOG_FILEPATH = os.path.join(LOG_DIR, LOG_FILENAME)


os.makedirs(LOG_DIR, exist_ok=True)


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(lineno)d - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)


file_handler = RotatingFileHandler(
    LOG_FILEPATH, maxBytes=1024 * 1024 * 10, backupCount=5
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


logger.addHandler(file_handler)
logger.addHandler(stream_handler)