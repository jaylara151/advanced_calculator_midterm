from app.operations import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
    PowerOperation,
    RootOperation,
    ModuloOperation,
    IntegerDivisionOperation,
    PercentageDifferenceOperation,
    PercentageChangeOperation,
)
from app.exceptions import InvalidInputError


class OperationFactory:
    """Factory class used to create calculator operation objects."""

    @staticmethod
    def create_operation(operation_name):
        """
        Return the correct operation object based on the operation name.

        Parameters:
            operation_name (str): The name of the operation.

        Returns:
            An operation object.

        Raises:
            InvalidInputError: If the operation name is not supported.
        """
        operations = {
            "add": AddOperation(),
            "subtract": SubtractOperation(),
            "multiply": MultiplyOperation(),
            "divide": DivideOperation(),
            "power": PowerOperation(),
            "root": RootOperation(),
            "modulo": ModuloOperation(),
            "int_divide": IntegerDivisionOperation(),
            "integer_divide": IntegerDivisionOperation(),
            "percent_diff": PercentageDifferenceOperation(),
            "percentage_difference": PercentageDifferenceOperation(),
            "percent_change": PercentageChangeOperation(),
            "percentage_change": PercentageChangeOperation(),
        }

        operation_name = operation_name.lower().strip()

        if operation_name not in operations:
            raise InvalidInputError(f"Unsupported operation: {operation_name}")

        return operations[operation_name]