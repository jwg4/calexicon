import unittest

from calexicon.internal.gregorian import is_gregorian_leap_year


class TestGregorian(unittest.TestCase):
    def test_is_gregorian_leap_year(self):
        self.assertTrue(is_gregorian_leap_year(2000))
        self.assertTrue(is_gregorian_leap_year(1984))
        self.assertFalse(is_gregorian_leap_year(1900))
        self.assertFalse(is_gregorian_leap_year(1901))

