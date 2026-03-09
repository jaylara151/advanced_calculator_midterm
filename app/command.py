class Command:
    """Base command class."""

    def execute(self):
        """Run the command."""
        raise NotImplementedError("Subclasses must implement execute().")


class CalculateCommand(Command):
    """Command used to perform a calculation."""

    def __init__(self, facade, operation_name, a, b):
        self.facade = facade
        self.operation_name = operation_name
        self.a = a
        self.b = b

    def execute(self):
        """Run the calculation."""
        return self.facade.calculate(self.operation_name, self.a, self.b)


class HistoryCommand(Command):
    """Command used to get calculation history."""

    def __init__(self, facade):
        self.facade = facade

    def execute(self):
        """Return the calculation history."""
        return self.facade.get_history()


class ClearHistoryCommand(Command):
    """Command used to clear calculation history."""

    def __init__(self, facade):
        self.facade = facade

    def execute(self):
        """Clear the calculation history."""
        self.facade.clear_history()


class SaveHistoryCommand(Command):
    """Command used to save history to a file."""

    def __init__(self, facade, file_path):
        self.facade = facade
        self.file_path = file_path

    def execute(self):
        """Save the history."""
        self.facade.save_history(self.file_path)


class LoadHistoryCommand(Command):
    """Command used to load history from a file."""

    def __init__(self, facade, file_path):
        self.facade = facade
        self.file_path = file_path

    def execute(self):
        """Load the history."""
        self.facade.load_history(self.file_path)