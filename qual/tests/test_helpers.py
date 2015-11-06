import unittest

from qual.helpers import ordinal, month_string

class TestOrdinal(unittest.TestCase):
    def test_valid_ordinal(self):
        self.assertEqual(ordinal(3), "3rd")

    def test_1st(self):
        self.assertEqual(ordinal(1), "1st")

    def test_2nd(self):
        self.assertEqual(ordinal(2), "2nd")

class TestMonthString(unittest.TestCase):
    def test_valid_month(self):
        self.assertEqual(month_string(11), "November")

