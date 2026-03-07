from datetime import datetime
import pandas as pd


class CalculationHistory:
    """Class used to store calculator history."""

    def __init__(self):
        """Create an empty calculation history list."""
        self.history = []

    def add_record(self, operation, a, b, result):
        """
        Add a calculation record to history.

        Parameters:
            operation (str): The operation name
            a: First number
            b: Second number
            result: Result of the calculation
        """
        record = {
            "operation": operation,
            "a": a,
            "b": b,
            "result": result,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.history.append(record)

    def get_history(self):
        """Return the full calculation history."""
        return self.history

    def clear_history(self):
        """Remove all records from history."""
        self.history.clear()

    def save_to_csv(self, file_path):
        """
        Save history to a CSV file using pandas.

        Parameters:
            file_path (str): Path to the CSV file
        """
        dataframe = pd.DataFrame(self.history)
        dataframe.to_csv(file_path, index=False)

    def load_from_csv(self, file_path):
        """
        Load history from a CSV file using pandas.

        Parameters:
            file_path (str): Path to the CSV file
        """
        dataframe = pd.read_csv(file_path)
        self.history = dataframe.to_dict(orient="records")