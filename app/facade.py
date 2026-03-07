from app.calculator import Calculator
from app.operation_factory import OperationFactory


class CalculatorFacade:
    """Facade class that provides a simple way to perform calculations."""

    def __init__(self):
        """Create a calculator facade with a calculator instance."""
        self.calculator = Calculator()

    def calculate(self, operation_name, a, b):
        """
        Perform a calculation using the operation name and two numbers.

        Parameters:
            operation_name (str): The name of the operation to perform.
            a: First number
            b: Second number

        Returns:
            The result of the calculation
        """
        operation = OperationFactory.create_operation(operation_name)
        return self.calculator.calculate(operation, a, b)