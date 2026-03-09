from app.repl import CalculatorREPL
from app.command import (
    CalculateCommand,
    HistoryCommand,
    ClearHistoryCommand,
    SaveHistoryCommand,
    LoadHistoryCommand,
)
from app.facade import CalculatorFacade


def test_repl_initializes():
    repl = CalculatorREPL()
    assert repl is not None
    assert repl.running is True


def test_repl_exit_command():
    repl = CalculatorREPL()
    repl.handle_command("exit")
    assert repl.running is False


def test_repl_clear_command():
    repl = CalculatorREPL()
    repl.facade.calculate("add", 5, 3)
    repl.handle_command("clear")
    assert repl.facade.get_history() == []


def test_repl_history_command_with_no_history():
    repl = CalculatorREPL()
    repl.handle_command("history")
    assert repl.facade.get_history() == []


def test_repl_valid_calculation_command():
    repl = CalculatorREPL()
    repl.handle_command("add 5 3")
    history = repl.facade.get_history()
    assert len(history) == 1
    assert history[0]["result"] == 8


def test_repl_invalid_command_format():
    repl = CalculatorREPL()
    repl.handle_command("add 5")
    assert repl.running is True


def test_repl_invalid_number():
    repl = CalculatorREPL()
    repl.handle_command("add five 3")
    assert repl.running is True


def test_calculate_command():
    facade = CalculatorFacade()
    command = CalculateCommand(facade, "add", 5, 3)
    result = command.execute()
    assert result == 8


def test_history_command():
    facade = CalculatorFacade()
    facade.calculate("add", 5, 3)
    command = HistoryCommand(facade)
    records = command.execute()
    assert len(records) == 1


def test_clear_history_command():
    facade = CalculatorFacade()
    facade.calculate("multiply", 6, 7)
    command = ClearHistoryCommand(facade)
    command.execute()
    assert facade.get_history() == []


def test_save_and_load_history_commands(tmp_path):
    facade = CalculatorFacade()
    facade.calculate("subtract", 10, 4)

    file_path = tmp_path / "history.csv"

    save_command = SaveHistoryCommand(facade, file_path)
    save_command.execute()

    new_facade = CalculatorFacade()
    load_command = LoadHistoryCommand(new_facade, file_path)
    load_command.execute()

    records = new_facade.get_history()
    assert len(records) == 1
    assert records[0]["operation"] == "subtract"