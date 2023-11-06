# Testy - Zadanie 9
# test_my_function.py
import unittest
from lab5_9 import my_function


class TestMyFunction(unittest.TestCase):

    def test_square(self):
        """Test case for x=1, should return y squared."""
        self.assertEqual(my_function(1, 3), 9)

    def test_sum(self):
        """Test case for x=2, should return sum of x and y."""
        self.assertEqual(my_function(2, 4), 6)

    def test_product(self):
        """Test case for x=3, should return product of x and y."""
        self.assertEqual(my_function(3, 1), 3)

    def test_zero(self):
        """Test case for x=4, should return 0."""
        self.assertEqual(my_function(4, 9), 0)

    def test_none(self):
        """Test case for other values of x, should return None."""
        self.assertIsNone(my_function(5, 10))

    def test_negative(self):
        """Test case for negative values, should behave accordingly."""
        self.assertEqual(my_function(1, -3), 9)  # Negative squared
        self.assertEqual(my_function(2, -4), -2)  # Sum with negative
        self.assertEqual(my_function(3, -1), -3)  # Product with negative
        self.assertEqual(my_function(4, -9), 0)   # Should still return 0
        self.assertIsNone(my_function(-1, 3))     # Undefined case, should return None


if __name__ == '__main__':
    unittest.main()
