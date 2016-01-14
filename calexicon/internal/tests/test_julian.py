import unittest

from datetime import date as vanilla_date

from calexicon.internal.julian import distant_julian_to_gregorian, julian_to_gregorian
from calexicon.internal.julian import is_julian_leap_year


class TestJulian(unittest.TestCase):
    def test_is_gregorian_leap_year(self):
        self.assertTrue(is_julian_leap_year(2000))
        self.assertTrue(is_julian_leap_year(1984))
        self.assertTrue(is_julian_leap_year(1900))
        self.assertFalse(is_julian_leap_year(1901))

    def test_distant_julian_to_gregorian(self):
        self.assertEqual(distant_julian_to_gregorian(9999, 12, 1), (10000, 2, 12))

    def test_julian_to_gregorian(self):
        self.assertEqual(julian_to_gregorian(1984, 2, 29), vanilla_date(1984, 3, 13))
