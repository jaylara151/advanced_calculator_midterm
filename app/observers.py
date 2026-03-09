class Observer:
    """Base observer class."""

    def update(self, record):
        """React to an update."""
        raise NotImplementedError("Subclasses must implement update().")


class LoggingObserver(Observer):
    """Observer that stores calculation records for logging-like tracking."""

    def __init__(self):
        """Create an empty list of observed records."""
        self.logged_records = []

    def update(self, record):
        """Store the new calculation record."""
        self.logged_records.append(record)


class AutoSaveObserver(Observer):
    """Observer that stores calculation records for autosave-like tracking."""

    def __init__(self):
        """Create an empty list of autosaved records."""
        self.saved_records = []

    def update(self, record):
        """Store the new calculation record."""
        self.saved_records.append(record)