import unittest

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

# class TestCalculator(unittest.TestCase):
#     def setUp(self): # setUp jest jak konstruktor dla zwykłej klasy, zostanie wywołany na początku testów
#         # Given
#         print("Setting up")
#         self.a = 5
#         self.b = 3
#         self.calculator = Calculator(self.a, self.b)
#     def tearDown(self):
#         print("Done")
#     def test_add(self):
#         # When
#         print("Test add")
#         result = self.calculator.add()
#         # Then
#         sum_a_b = self.a + self.b
#         self.assertEqual(result, sum_a_b)
#     def test_subtract(self):
#         print("Test subtract")
#         difference_a_b = self.a - self.b
#         self.assertEqual(self.calculator.subtract(), difference_a_b)
#     def test_multiply(self):
#         print("Test multiply")
#         value = self.a * self.b
#         self.assertEqual(self.calculator.multiply(), value)
#     def test_divide(self):
#         print("Test divide")
#         value = self.a / self.b
#         self.assertEqual(self.calculator.divide(), value)

# run tests from console: python -m unittest discover <tests_directory_name>
from unittest.mock import patch

class SomeClass:
    def something(self):
        return "something"

with patch.object(SomeClass, "something", return_value="other") as new_mock:
    some = SomeClass()
    print(some.something())