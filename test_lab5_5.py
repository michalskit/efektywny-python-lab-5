# Testy - Zadanie 5
import unittest
from lab5_5 import accepts


class TestAcceptsDecorator(unittest.TestCase):

    def test_accepts_correct_types(self):
        @accepts(str)
        def capitalize(word):
            return word[0].upper() + word[1:]
        
        self.assertEqual(capitalize('ola'), 'Ola')

    def test_accepts_incorrect_types_raises_type_error(self):
        @accepts(str)
        def capitalize(word):
            return word[0].upper() + word[1:]
        
        with self.assertRaises(TypeError):
            capitalize(2)

    def test_accepts_with_multiple_types(self):
        @accepts(float, int)
        def static_pow(base, exp):
            return base ** exp 

        self.assertEqual(static_pow(2., 2), 4.)

    def test_accepts_with_multiple_types_incorrect_base_type(self):
        @accepts(float, int)
        def static_pow(base, exp):
            return base ** exp 
        
        with self.assertRaises(TypeError):
            static_pow('x', 10)

    def test_accepts_with_multiple_types_incorrect_exp_type(self):
        @accepts(float, int)
        def static_pow(base, exp):
            return base ** exp 

        with self.assertRaises(TypeError):
            static_pow(2, 2.2)

    def test_accepts_with_keyword_arguments(self):
        @accepts(float, int)
        def static_pow(base, exp):
            return base ** exp 

        self.assertEqual(static_pow(base=2., exp=2), 4.)
        self.assertEqual(static_pow(2., exp=2), 4.)


if __name__ == '__main__':
    unittest.main()
