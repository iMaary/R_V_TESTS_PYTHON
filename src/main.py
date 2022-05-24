import numbers


class CalculatorA(object):
    def sum(self, a: int, b: int) -> int:
        self._check_type(a)
        self._check_type(b)
        return a + b

    def _check_type(self, opt) -> None:
        if not isinstance(opt, numbers.Number):
            raise CalculatorError(f'{opt} não é um número')


class CalculatorError(Exception):
    def __init__(self, error_msg: str):
        pass


class CalculatorB:
    def soma(x, y) -> float:
        return x + y


if __name__ == "__main__":
    print("Testing...")