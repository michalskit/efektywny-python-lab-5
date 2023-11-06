# Testy - Zadanie 6
import unittest
from lab5_6 import returns

class TestReturnsDecorator(unittest.TestCase):
    
    def test_single_return_type(self):
        @returns(str)
        def str_only_identity(word):
            return word

        # Test with correct return type
        self.assertEqual(str_only_identity('hello'), 'hello')

        # Test with incorrect return type
        with self.assertRaises(TypeError):
            str_only_identity(10)
    
    def test_multiple_return_types(self):
        @returns(int, int)
        def split_indices(x):
            return x[0], x[1]

        # Test with correct return types
        self.assertEqual(split_indices(x=[6,9]), (6,9))

        # Test with incorrect return types
        with self.assertRaises(TypeError):
            split_indices('AB')

# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main()


