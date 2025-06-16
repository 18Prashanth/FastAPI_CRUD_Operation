import logging
from logging.handlers import RotatingFileHandler

log_file = "app.log"
handler = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger("fastapi-app")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
