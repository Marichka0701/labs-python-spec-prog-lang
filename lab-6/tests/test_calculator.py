import unittest
from classes.Calculator import Calculator
from classes.Operation import Addition, Subtraction, Multiplication, Division, SquareRoot

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the Calculator instance before each test"""
        self.calc = Calculator()

    def test_addition(self):
        """Test addition operation"""
        result = self.calc.perform_operation('+', 5, 3)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        """Test subtraction operation"""
        result = self.calc.perform_operation('-', 10, 4)
        self.assertEqual(result, 6)

    def test_multiplication(self):
        """Test multiplication operation"""
        result = self.calc.perform_operation('*', 3, 7)
        self.assertEqual(result, 21)

    def test_division(self):
        """Test division operation"""
        result = self.calc.perform_operation('/', 20, 4)
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        """Test division by zero raises error"""
        with self.assertRaises(ZeroDivisionError):
            self.calc.perform_operation('/', 10, 0)

    def test_square_root(self):
        """Test square root operation"""
        result = self.calc.perform_operation('sqrt', 16)
        self.assertEqual(result, 4)

    def test_invalid_operator(self):
        """Test invalid operator raises ValueError"""
        with self.assertRaises(ValueError):
            self.calc.perform_operation('%', 5, 3)


if __name__ == "__main__":
    unittest.main()
