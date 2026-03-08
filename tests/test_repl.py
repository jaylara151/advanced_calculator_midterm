from app.repl import CalculatorREPL


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