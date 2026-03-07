from dotenv import load_dotenv
import os

load_dotenv()


class AppConfig:
    """Class used to load calculator settings from environment variables."""

    def __init__(self):
        """Load configuration values from the environment."""
        self.max_history = int(os.getenv("CALC_MAX_HISTORY", 100))
        self.precision = int(os.getenv("CALC_PRECISION", 2))
        self.log_level = os.getenv("CALC_LOG_LEVEL", "INFO")
        self.history_file = os.getenv("CALC_HISTORY_FILE", "data/calculator_history.csv")
        self.log_file = os.getenv("CALC_LOG_FILE", "logs/calculator.log")