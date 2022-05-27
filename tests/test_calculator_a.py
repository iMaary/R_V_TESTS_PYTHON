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


@pytest.mark.parametrize("a, b, wrong_result", [(1, 1, 3), (4, 4, 6)])
def test_sum_diff_results(a, b, wrong_result):
    calc = CalculatorA()
    assert calc.sum(a, b) != wrong_result


@pytest.mark.parametrize("a, b, result",
                         [
                             (2, "5", 7),
                             ("4", "4", 8),
                             ("1", 2, 3)
                         ])
def test_sum_strings(a, b, result):
    calc = CalculatorA()
    with pytest.raises(CalculatorError):
        calc.sum(a, b)
