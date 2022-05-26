from src.main import CalculatorA, CalculatorError
import pytest


@pytest.mark.parametrize("a, b, res", [(1, 1, 2), (2, 3, 5)])
def test_sum(a, b, res):
    calculator = CalculatorA()
    assert calculator.sum(a, b) == res


@pytest.mark.parametrize("a, b, res", [(1, 1, 1), (2, 3, 6)])
def test_mult(a, b, res):
    calculator = CalculatorA()
    assert calculator.mult(a, b) == res


@pytest.mark.parametrize("a, b, res", [(2, 2, 1), (10, 2, 5)])
def test_div(a, b, res):
    calculator = CalculatorA()
    assert calculator.div(a, b) == res


@pytest.mark.parametrize("a, b, res", [(7, 5, 2), (8, 3, 5)])
def test_subtract(a, b, res):
    calculator = CalculatorA()
    assert calculator.sub(a, b) == res


@pytest.mark.parametrize("a, b, res", [(3, 2, 9), (2, 2, 4)])
def test_pot(a, b, res):
    calculator = CalculatorA()
    assert calculator.pot(a, b) == res
