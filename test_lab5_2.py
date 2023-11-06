# Testy - Zadanie 2
import unittest
from lab5_2 import calculate_density


class TestCalculateDensity(unittest.TestCase):

    def test_default_units(self):
        self.assertAlmostEqual(calculate_density(1000, 1), 1000)

    def test_conversion_to_kg_and_cubic_meters(self):
        self.assertAlmostEqual(calculate_density(1000, 1e6, 'g', 'cm^3'), 1)
        self.assertAlmostEqual(calculate_density(1500, 1500000, 'g', 'cm^3'), 1)

    def test_unsupported_mass_unit(self):
        with self.assertRaises(NotImplementedError):
            calculate_density(1000, 1, 'pounds', 'm^3')

    def test_unsupported_volume_unit(self):
        with self.assertRaises(NotImplementedError):
            calculate_density(1000, 1, 'kg', 'liters')

    def test_zero_volume(self):
        with self.assertRaises(ValueError):
            calculate_density(1000, 0)


if __name__ == '__main__':
    unittest.main()

