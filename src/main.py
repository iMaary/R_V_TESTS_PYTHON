import numbers


class CalculatorA(object):
    def sum(self, a: int, b: int) -> int:
        self._check_type(a)
        self._check_type(b)
        return a + b

    def mult(self, a: int, b: int) -> int:
        self._check_type(a)
        self._check_type(b)
        return a * b


    def div(self, a: int, b: int) -> int:
        self._check_type(a)
        self._check_type(b)
        return a / b

    
    def sub(self, a: int, b: int) -> int:
        self._check_type(a)
        self._check_type(b)
        return a - b

    def pot(self, a: int, b: int) -> int:
        self._check_type(a)
        self._check_type(b)
        temp = a
        for _ in range(b - 1):
            a = a * temp
        return a

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
