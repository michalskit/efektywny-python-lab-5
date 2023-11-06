# Testy - Zadanie 3
import unittest
from lab5_3 import timeit

class TestTimeitDecorator(unittest.TestCase):
    
    def test_timeit_return_value(self):
        @timeit
        def dummy_function():
            return "Hello, World!"
            
        result = dummy_function()
        self.assertEqual(result, "Hello, World!")

    def test_timeit_with_args(self):
        @timeit
        def add(x, y):
            return x + y
            
        result = add(5, 7)
        self.assertEqual(result, 12)

    def test_timeit_with_kwargs(self):
        @timeit
        def add(x=0, y=0):
            return x + y
            
        result = add(x=5, y=7)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()




