import pytest

from app.calculator import Calculator
from app.facade import CalculatorFacade
from app.exceptions import DivisionByZeroError, NegativeRootError, InvalidInputError
from app.operation_factory import OperationFactory
from app.operations import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
    PowerOperation,
    RootOperation,
    ModuloOperation,
    IntegerDivisionOperation,
    PercentageDifferenceOperation,
    PercentageChangeOperation,
)


def test_add_operation():
    calculator = Calculator()
    result = calculator.calculate(AddOperation(), 5, 3)
    assert result == 8


def test_subtract_operation():
    calculator = Calculator()
    result = calculator.calculate(SubtractOperation(), 10, 4)
    assert result == 6


def test_multiply_operation():
    calculator = Calculator()
    result = calculator.calculate(MultiplyOperation(), 6, 7)
    assert result == 42


def test_divide_operation():
    calculator = Calculator()
    result = calculator.calculate(DivideOperation(), 20, 5)
    assert result == 4


def test_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(DivisionByZeroError):
        calculator.calculate(DivideOperation(), 10, 0)


def test_power_operation():
    calculator = Calculator()
    result = calculator.calculate(PowerOperation(), 2, 3)
    assert result == 8


def test_root_operation():
    calculator = Calculator()
    result = calculator.calculate(RootOperation(), 9, 2)
    assert result == 3


def test_negative_even_root():
    calculator = Calculator()
    with pytest.raises(NegativeRootError):
        calculator.calculate(RootOperation(), -16, 2)


def test_modulo_operation():
    calculator = Calculator()
    result = calculator.calculate(ModuloOperation(), 10, 3)
    assert result == 1


def test_integer_division_operation():
    calculator = Calculator()
    result = calculator.calculate(IntegerDivisionOperation(), 10, 3)
    assert result == 3


def test_percentage_difference_operation():
    calculator = Calculator()
    result = calculator.calculate(PercentageDifferenceOperation(), 80, 100)
    assert result == pytest.approx(22.2222, rel=1e-3)


def test_percentage_change_operation():
    calculator = Calculator()
    result = calculator.calculate(PercentageChangeOperation(), 80, 100)
    assert result == 25


def test_factory_creates_add_operation():
    operation = OperationFactory.create_operation("add")
    result = operation.execute(5, 3)
    assert result == 8


def test_factory_creates_divide_operation():
    operation = OperationFactory.create_operation("divide")
    result = operation.execute(20, 5)
    assert result == 4


def test_factory_creates_power_operation():
    operation = OperationFactory.create_operation("power")
    result = operation.execute(2, 3)
    assert result == 8


def test_factory_rejects_invalid_operation():
    with pytest.raises(InvalidInputError):
        OperationFactory.create_operation("banana")


def test_facade_add_operation():
    facade = CalculatorFacade()
    result = facade.calculate("add", 5, 3)
    assert result == 8


def test_facade_divide_operation():
    facade = CalculatorFacade()
    result = facade.calculate("divide", 20, 5)
    assert result == 4


def test_facade_power_operation():
    facade = CalculatorFacade()
    result = facade.calculate("power", 2, 3)
    assert result == 8


def test_facade_invalid_operation():
    facade = CalculatorFacade()
    with pytest.raises(InvalidInputError):
        facade.calculate("banana", 5, 3)