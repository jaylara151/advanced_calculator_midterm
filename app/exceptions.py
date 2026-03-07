class CalculatorError(Exception):
    """Base exception class for calculator errors."""
    pass


class InvalidInputError(CalculatorError):
    """Raised when the user gives invalid input."""
    pass


class InvalidNumberError(CalculatorError):
    """Raised when a number is invalid for the operation."""
    pass


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""
    pass


class NegativeRootError(CalculatorError):
    """Raised when trying to take an even root of a negative number."""
    pass