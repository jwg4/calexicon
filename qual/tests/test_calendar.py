import unittest

from datetime import date

import qual

class TestProlepticGregorianCalendar(unittest.TestCase):
    def setUp(self):
        self.calendar = qual.ProlepticGregorianCalendar()

    def check_valid_date(self, year, month, day):
        d = self.calendar.date(year, month, day)
        self.assertIsNotNone(d)

    def test_leap_year_from_before_1582(self):
        """Pope Gregory introduced the calendar in 1582"""
        self.check_valid_date(1200, 2, 29)
