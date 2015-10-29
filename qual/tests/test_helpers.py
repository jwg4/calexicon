import unittest

from qual.helpers import ordinal, month_string

class TestOrdinal(unittest.TestCase):
    def test_valid_ordinal(self):
        self.assertEqual(ordinal(3), "3rd")

class TestMonthString(unittest.TestCase):
    def test_valid_month(self):
        self.assertEqual(month_string(11), "November")

