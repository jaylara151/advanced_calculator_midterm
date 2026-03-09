from app.history import CalculationHistory
from app.facade import CalculatorFacade
import os 
from app.logger_setup import get_logger 
from app.observers import LoggingObserver, AutoSaveObserver

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


def test_save_to_csv(tmp_path):
    history = CalculationHistory()
    history.add_record("add", 5, 3, 8)

    file_path = tmp_path / "history.csv"
    history.save_to_csv(file_path)

    assert file_path.exists()


def test_load_from_csv(tmp_path):
    history = CalculationHistory()
    history.add_record("multiply", 6, 7, 42)

    file_path = tmp_path / "history.csv"
    history.save_to_csv(file_path)

    new_history = CalculationHistory()
    new_history.load_from_csv(file_path)

    records = new_history.get_history()

    assert len(records) == 1
    assert records[0]["operation"] == "multiply"
    assert records[0]["result"] == 42


def test_facade_save_and_load_history(tmp_path):
    facade = CalculatorFacade()
    facade.calculate("subtract", 10, 4)

    file_path = tmp_path / "history.csv"
    facade.save_history(file_path)

    new_facade = CalculatorFacade()
    new_facade.load_history(file_path)

    records = new_facade.get_history()

    assert len(records) == 1
    assert records[0]["operation"] == "subtract"
    assert records[0]["result"] == 6

def test_logger_is_created():
    logger = get_logger()
    assert logger is not None


def test_log_file_path_exists():
    logger = get_logger()
    assert logger.name == "calculator_app"


def test_logging_observer_updates():
    observer = LoggingObserver()

    record = {
        "operation": "add",
        "a": 5,
        "b": 3,
        "result": 8,
        "timestamp": "2026-03-09 10:00:00",
    }

    observer.update(record)

    assert len(observer.logged_records) == 1
    assert observer.logged_records[0]["operation"] == "add"


def test_autosave_observer_updates():
    observer = AutoSaveObserver()

    record = {
        "operation": "multiply",
        "a": 6,
        "b": 7,
        "result": 42,
        "timestamp": "2026-03-09 10:00:00",
    }

    observer.update(record)

    assert len(observer.saved_records) == 1
    assert observer.saved_records[0]["result"] == 42


def test_facade_notifies_observers():
    facade = CalculatorFacade()
    facade.calculate("add", 5, 3)

    logging_observer = facade.observers[0]
    autosave_observer = facade.observers[1]

    assert len(logging_observer.logged_records) == 1
    assert len(autosave_observer.saved_records) == 1
    assert logging_observer.logged_records[0]["operation"] == "add"
    assert autosave_observer.saved_records[0]["result"] == 8