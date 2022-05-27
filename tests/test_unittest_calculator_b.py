from src.main import CalculatorB
import unittest


class TestSomaUnittest(unittest.TestCase):
    def test_return_soma_10_10(self):
        self.assertEqual(CalculatorB.soma(10, 10), 20)
