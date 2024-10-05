import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test for addition method
    def test_addition(self):
        """Test the add method of SimpleCalculator."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Basic test case
        self.assertEqual(self.calc.add(-1, 1), 0)  # Negative and positive
        self.assertEqual(self.calc.add(0, 0), 0)  # Zero
        self.assertEqual(self.calc.add(-5, -5), -10)  # Two negative numbers

    # Test for subtraction method
    def test_subtraction(self):
        """Test the subtract method of SimpleCalculator."""
        self.assertEqual(self.calc.subtract(10, 5), 5)  # Basic test case
        self.assertEqual(self.calc.subtract(-1, 1), -2)  # Negative and positive
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Zero
        self.assertEqual(self.calc.subtract(-5, -5), 0)  # Two negative numbers
        self.assertEqual(self.calc.subtract(5, 10), -5)  # Resulting in negative

    # Test for multiplication method
    def test_multiplication(self):
        """Test the multiply method of SimpleCalculator."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Basic test case
        self.assertEqual(self.calc.multiply(-1, 1), -1)  # Negative and positive
        self.assertEqual(self.calc.multiply(0, 100), 0)  # Multiplication with zero
        self.assertEqual(self.calc.multiply(-5, -5), 25)  # Two negative numbers
        self.assertEqual(self.calc.multiply(5, -2), -10)  # Positive and negative

    # Test for division method
    def test_division(self):
        """Test the divide method of SimpleCalculator."""
        self.assertEqual(self.calc.divide(10, 2), 5)  # Basic test case
        self.assertEqual(self.calc.divide(-10, 2), -5)  # Negative numerator
        self.assertEqual(self.calc.divide(10, -2), -5)  # Negative denominator
        self.assertEqual(self.calc.divide(-10, -2), 5)  # Both negative
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero
        self.assertEqual(self.calc.divide(0, 10), 0)  # Zero numerator

    # Additional edge case for divide method
    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(1, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == '__main__':
    unittest.main()
