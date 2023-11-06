# Testy - Zadanie 8
import unittest
from lab5_8 import zlozenie


class TestZlozenieDecorator(unittest.TestCase):

    def test_single_increment(self):
        @zlozenie(1)
        def increment(x):
            return x + 1
        self.assertEqual(increment(5), 6)

    def test_triple_increment(self):
        @zlozenie(3)
        def increment(x):
            return x + 1
        self.assertEqual(increment(5), 8)

    def test_double_square(self):
        @zlozenie(2)
        def square(x):
            return x * x
        self.assertEqual(square(3), 81)

    def test_character_shift(self):
        @zlozenie(5)
        def shift(word):
            return "".join(chr(ord(l) + 1) for l in word)
        self.assertEqual(shift("alamakota"), "fqfrfptyf")

    def test_zero_times(self):
        @zlozenie(0)
        def do_nothing(x):
            return x + 1
        self.assertEqual(do_nothing(5), 5)


if __name__ == '__main__':
    unittest.main()