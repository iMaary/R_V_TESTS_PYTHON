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
