from app.calculator import Calculator
from app.operation_factory import OperationFactory
from app.history import CalculationHistory


class CalculatorFacade:
    """Facade class that provides a simple way to perform calculations."""

    def __init__(self):
        """Create a calculator facade with calculator and history instances."""
        self.calculator = Calculator()
        self.history = CalculationHistory()

    def calculate(self, operation_name, a, b):
        """
        Perform a calculation using the operation name and two numbers.

        Parameters:
            operation_name (str): The name of the operation to perform
            a: First number
            b: Second number

        Returns:
            The result of the calculation
        """
        operation = OperationFactory.create_operation(operation_name)
        result = self.calculator.calculate(operation, a, b)
        self.history.add_record(operation_name, a, b, result)
        return result

    def get_history(self):
        """Return the full calculation history."""
        return self.history.get_history()

    def clear_history(self):
        """Clear the calculation history."""
        self.history.clear_history()

    def save_history(self, file_path):
        """Save history to a CSV file."""
        self.history.save_to_csv(file_path)

    def load_history(self, file_path):
        """Load history from a CSV file."""
        self.history.load_from_csv(file_path)