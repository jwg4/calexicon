import unittest

from calexicon.constants import number_of_days_in_400_gregorian_years


class TestConstants(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(number_of_days_in_400_gregorian_years, 365 * 400 + 97)
