import logging
import os

from app.config import AppConfig


def get_logger():
    """Create and return a configured logger for the calculator app."""
    config = AppConfig()

    log_directory = os.path.dirname(config.log_file)
    if log_directory:
        os.makedirs(log_directory, exist_ok=True)

    logger = logging.getLogger("calculator_app")
    logger.setLevel(getattr(logging, config.log_level.upper(), logging.INFO))

    if not logger.handlers:
        file_handler = logging.FileHandler(config.log_file)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger