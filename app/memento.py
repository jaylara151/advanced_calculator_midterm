import copy


class HistoryMemento:
    """Memento class that stores a snapshot of calculation history."""

    def __init__(self, history_state):
        """Save a deep copy of the history state."""
        self._history_state = copy.deepcopy(history_state)

    def get_saved_state(self):
        """Return the saved history state."""
        return copy.deepcopy(self._history_state)


class HistoryCaretaker:
    """Caretaker class that manages undo and redo history states."""

    def __init__(self):
        """Create empty undo and redo stacks."""
        self.undo_stack = []
        self.redo_stack = []

    def save(self, history_state):
        """Save a new history state and clear redo stack."""
        self.undo_stack.append(HistoryMemento(history_state))
        self.redo_stack.clear()

    def undo(self, current_state):
        """
        Restore the previous history state.

        Returns:
            The restored state, or the current state if undo is not possible.
        """
        if not self.undo_stack:
            return current_state

        self.redo_stack.append(HistoryMemento(current_state))
        memento = self.undo_stack.pop()
        return memento.get_saved_state()

    def redo(self, current_state):
        """
        Restore the next undone history state.

        Returns:
            The restored state, or the current state if redo is not possible.
        """
        if not self.redo_stack:
            return current_state

        self.undo_stack.append(HistoryMemento(current_state))
        memento = self.redo_stack.pop()
        return memento.get_saved_state()