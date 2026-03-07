from app.exceptions import DivisionByZeroError, NegativeRootError


class AddOperation:
    """Class for addition."""

    def execute(self, a, b):
        """Return the sum of two numbers."""
        return a + b


class SubtractOperation:
    """Class for subtraction."""

    def execute(self, a, b):
        """Return the difference of two numbers."""
        return a - b


class MultiplyOperation:
    """Class for multiplication."""

    def execute(self, a, b):
        """Return the product of two numbers."""
        return a * b


class DivideOperation:
    """Class for division."""

    def execute(self, a, b):
        """Return the quotient of two numbers."""
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero.")
        return a / b


class PowerOperation:
    """Class for exponentiation."""

    def execute(self, a, b):
        """Raise a number to the power of another number."""
        return a ** b


class RootOperation:
    """Class for roots."""

    def execute(self, a, b):
        """Return the b-th root of a."""
        if b == 0:
            raise DivisionByZeroError("Root degree cannot be zero.")
        if a < 0 and b % 2 == 0:
            raise NegativeRootError("Cannot take an even root of a negative number.")
        return a ** (1 / b)


class ModuloOperation:
    """Class for modulo."""

    def execute(self, a, b):
        """Return the remainder after division."""
        if b == 0:
            raise DivisionByZeroError("Cannot take modulo by zero.")
        return a % b


class IntegerDivisionOperation:
    """Class for integer division."""

    def execute(self, a, b):
        """Return the integer quotient after division."""
        if b == 0:
            raise DivisionByZeroError("Cannot perform integer division by zero.")
        return a // b


class PercentageDifferenceOperation:
    """Class for percentage difference."""

    def execute(self, a, b):
        """Return the percentage difference between two numbers."""
        average = (a + b) / 2
        if average == 0:
            raise DivisionByZeroError("Cannot calculate percentage difference when average is zero.")
        return abs(a - b) / average * 100


class PercentageChangeOperation:
    """Class for percentage change."""

    def execute(self, a, b):
        """
        Return the percentage change from a to b.
        Formula: ((new - old) / old) * 100
        Here, a is the old value and b is the new value.
        """
        if a == 0:
            raise DivisionByZeroError("Cannot calculate percentage change from zero.")
        return ((b - a) / a) * 100