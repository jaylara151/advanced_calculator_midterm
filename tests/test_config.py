from app.config import AppConfig


def test_config_loads_values():
    config = AppConfig()

    assert config.max_history == 100
    assert config.precision == 2
    assert config.log_level == "INFO"
    assert config.history_file == "data/calculator_history.csv"
    assert config.log_file == "logs/calculator.log"


def test_config_has_expected_attributes():
    config = AppConfig()

    assert hasattr(config, "max_history")
    assert hasattr(config, "precision")
    assert hasattr(config, "log_level")
    assert hasattr(config, "history_file")
    assert hasattr(config, "log_file")