from src.main import CalculatorA
# pytest already installed globally
# import pytest


def test_sum():
    calculator = CalculatorA()

    a = 5
    b = 2
    res = calculator.soma(a, b)

    assert res == 7
