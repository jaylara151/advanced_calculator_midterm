from app.history import CalculationHistory
from app.facade import CalculatorFacade


def test_add_record():
    history = CalculationHistory()
    history.add_record("add", 5, 3, 8)

    records = history.get_history()

    assert len(records) == 1
    assert records[0]["operation"] == "add"
    assert records[0]["a"] == 5
    assert records[0]["b"] == 3
    assert records[0]["result"] == 8
    assert "timestamp" in records[0]


def test_get_history():
    history = CalculationHistory()
    history.add_record("multiply", 6, 7, 42)

    records = history.get_history()

    assert len(records) == 1
    assert records[0]["operation"] == "multiply"


def test_clear_history():
    history = CalculationHistory()
    history.add_record("subtract", 10, 4, 6)
    history.clear_history()

    records = history.get_history()

    assert records == []


def test_facade_saves_history():
    facade = CalculatorFacade()
    facade.calculate("add", 5, 3)

    records = facade.get_history()

    assert len(records) == 1
    assert records[0]["operation"] == "add"
    assert records[0]["result"] == 8


def test_facade_clears_history():
    facade = CalculatorFacade()
    facade.calculate("multiply", 6, 7)
    facade.clear_history()

    records = facade.get_history()

    assert records == []