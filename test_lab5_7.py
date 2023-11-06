# Testy - Zadanie 7
import unittest
from lab5_7 import cached
from random import random

@cached
def mockup_func(*args, **kwargs):
    return random()

class TestCachedDecorator(unittest.TestCase):

    def test_single_evaluation(self):
        """ Test if the function with the same arguments is evaluated only once. """
        result1 = mockup_func(1, 2, 3)
        result2 = mockup_func(1, 2, 3)
        self.assertEqual(result1, result2)

    def test_diff_args_evaluation(self):
        """ Test if the function with different arguments is evaluated separately. """
        mockup_func.cache_reset()  # Reset cache to ensure a clean slate
        result1 = mockup_func(1, 2, 3)
        result2 = mockup_func(3, 2, 1)
        self.assertNotEqual(result1, result2)

    def test_keyword_args(self):
        """ Test if the function evaluates correctly with keyword arguments. """
        mockup_func.cache_reset()
        result1 = mockup_func(x=1, y=2)
        result2 = mockup_func(x=1, y=2)
        self.assertEqual(result1, result2)

    def test_mixed_args(self):
        """ Test if the function evaluates correctly with a mix of positional and keyword arguments. """
        mockup_func.cache_reset()
        result1 = mockup_func(1, y=2)
        result2 = mockup_func(1, y=2)
        self.assertEqual(result1, result2)

    def test_cache_reset(self):
        """ Test if the cache is correctly reset. """
        mockup_func.cache_reset()
        result1 = mockup_func(1, 2, 3)
        mockup_func.cache_reset()
        result2 = mockup_func(1, 2, 3)
        self.assertNotEqual(result1, result2)

    def test_cache_status(self):
        """ Test if the cache_status returns the correct string. """
        mockup_func.cache_reset()
        mockup_func(1, 2, 3)
        mockup_func(1, 2, 3)
        status = mockup_func.cache_status()
        self.assertEqual(status, 'Function mockup_func called 2 times, evaluated 1 times')

if __name__ == '__main__':
    unittest.main()
