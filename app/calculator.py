class Calculator:
    """Basic calculator class that uses operation objects."""

    def calculate(self, operation, a, b):
        """
        Perform a calculation using the given operation object.

        Parameters:
            operation: an object with an execute(a, b) method
            a: first number
            b: second number

        Returns:
            The result of the operation
        """
        return operation.execute(a, b)