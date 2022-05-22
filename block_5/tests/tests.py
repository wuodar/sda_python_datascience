import unittest

class Calculator:
    def __init__(self, val_a, val_b):
        self.val_a = val_a
        self.val_b = val_b

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.a = 5
        self.b = 3
        self.calculator = Calculator(self.a, self.b)

    def test_add(self):
        value = self.a + self.b
        self.assertEqual(self.calculator.addition(), value)