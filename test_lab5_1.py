# Testy - Zadanie 1
import unittest
from lab5_1 import podziel_liczby


class TestPodzielLiczby(unittest.TestCase):

    def test_dzielenie_poprawne(self):
        self.assertEqual(podziel_liczby(10, 2), 5.0)

    def test_dzielenie_przez_zero(self):
        self.assertIsNone(podziel_liczby(5, 0))

    def test_dzielenie_niepoprawne_typy(self):
        self.assertIsNone(podziel_liczby('5', '2'))

    def test_dzielenie_ujemne(self):
        self.assertEqual(podziel_liczby(-10, 2), -5.0)

    def test_dzielenie_przez_ujemne(self):
        self.assertEqual(podziel_liczby(10, -2), -5.0)

    def test_dzielenie_ujemne_przez_ujemne(self):
        self.assertEqual(podziel_liczby(-10, -2), 5.0)

    def test_dzielenie_przez_jeden(self):
        self.assertEqual(podziel_liczby(5, 1), 5)

    def test_dzielenie_zerem(self):
        self.assertEqual(podziel_liczby(0, 5), 0)


if __name__ == '__main__':
    unittest.main()