import unittest

from calexicon.internal.julian import distant_julian_to_gregorian, julian_to_gregorian


class TestJulian(unittest.TestCase):
    def test_distant_julian_to_gregorian(self):
        self.assertEqual(distant_julian_to_gregorian(9999, 12, 1), (10000, 2, 12))

    def test_julian_to_gregorian(self):
        self.assertEqual(julian_to_gregorian(1984, 2, 29), (1984, 3, 13))
