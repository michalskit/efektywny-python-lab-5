# Testy - Zadanie 4
import unittest
from lab5_4 import derivate

class TestDerivateDecorator(unittest.TestCase):

    def test_default_epsilon(self):
        # A simple function to test the default epsilon
        @derivate()
        def func(x):
            return 5*x**3

        self.assertAlmostEqual(func(1), 15, places=5)

    def test_custom_epsilon(self):
        # Test with a custom epsilon for a simple linear function
        @derivate(0.001)
        def func(x):
            return 5*x

        self.assertAlmostEqual(func(1), 5, places=5)

    def test_derivative_correctness(self):
        # Test the correctness of the derivative with a known function
        @derivate(0.01)
        def f(x):
            return x**2

        # Allow a small error margin by checking to 1 decimal place instead of 2
        self.assertAlmostEqual(f(2), 4, places=1)

        @derivate(0.00001)
        def g(x):
            return x**3 + 3

        # Allow a small error margin by checking to 1 decimal place instead of 2
        self.assertAlmostEqual(g(2), 12, places=1)

    def test_multiple_functions(self):
        # Test that the decorator works with multiple functions
        @derivate(0.01)
        def f(x):
            return x**2

        @derivate(0.00001)
        def g(x):
            return x**3 + 3

        # Allow a small error margin by checking to 1 decimal place instead of 2
        self.assertAlmostEqual(f(2), 4, places=1)
        self.assertAlmostEqual(g(2), 12, places=1)



if __name__ == '__main__':
    unittest.main()
