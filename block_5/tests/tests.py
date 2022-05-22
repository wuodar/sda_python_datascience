import unittest

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.a = 5
        self.b = 3
        self.calculator = Calculator(self.a, self.b)

    def test_add(self):
        value = self.a + self.b
        self.assertEqual(self.calculator.addition(), value)