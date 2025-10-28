import logging
import os
from datetime import datetime

os.makedirs("test_logs", exist_ok=True)    # Создание папки для логов
LOG_FILE = os.path.join("test_logs", f"test_run_{datetime.now().strftime('%d-%m-%Y')}.log")

logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)
logger.propagate = False    # Отключение дублирования логгов в root-логгер(консоль)

if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE, mode='a', encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def get_logger():
    return logger