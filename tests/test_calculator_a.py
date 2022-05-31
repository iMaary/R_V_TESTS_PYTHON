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


@pytest.mark.parametrize("a, b, wrong_result", [(4, 8, 10), (4, 42, 0)])
def test_sub_diff_results(a, b, wrong_result):
    calc = CalculatorA()
    assert calc.sub(a, b) != wrong_result


@pytest.mark.parametrize("a, b, wrong_result", [(56, 8, 7), (1, 0, 6)])
def test_mult_diff_results(a, b, wrong_result):
    calc = CalculatorA()
    assert calc.mult(a, b) != wrong_result


@pytest.mark.parametrize("a, b, wrong_result", [(2, 4, 5), (20, 4, 6)])
def test_pot_diff_results(a, b, wrong_result):
    calc = CalculatorA()
    assert calc.pot(a, b) != wrong_result


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


@pytest.mark.parametrize("a, b, result",
                         [
                             (5, "2", 3),
                             ("4", "4", 0),
                             ("2", 1, 1)
                         ])
def test_sub_strings(a, b, result):
    calc = CalculatorA()
    with pytest.raises(CalculatorError):
        calc.sub(a, b)


@pytest.mark.parametrize("a, b, result",
                         [
                             (5, "2", 10),
                             ("4", "4", 16),
                             ("1", 2, 2)
                         ])
def test_mult_strings(a, b, result):
    calc = CalculatorA()
    with pytest.raises(CalculatorError):
        calc.mult(a, b)


@pytest.mark.parametrize("a, b, result",
                         [
                             (5, "2", 25),
                             ("2", "3", 8),
                             ("1", 2, 1)
                         ])
def test_pot_strings(a, b, result):
    calc = CalculatorA()
    with pytest.raises(CalculatorError):
        calc.pot(a, b)


def sum_stress_test(a, b, result):
    calc = CalculatorA()
    a = 999999999999
    b = 999999999999
    assert calc.sum(a, b) == result


def sub_stress_test(a, b, result):
    calc = CalculatorA()
    a = 999999999999
    b = 999999999999
    assert calc.sum(a, b) == result


def mult_stress_test(a, b, result):
    calc = CalculatorA()
    a = 999999999999
    b = 999999999999
    assert calc.sum(a, b) == result


def pot_stress_test(a, b, result):
    calc = CalculatorA()
    a = 999999999999
    b = 999999999999
    assert calc.sum(a, b) == result
