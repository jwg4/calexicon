import unittest

from datetime import date

import qual

class TestProlepticGregorianCalendar(unittest.TestCase):
    def setUp(self):
        self.calendar = qual.ProlepticGregorianCalendar()

    def check_valid_date(self, year, month, day):
        d = self.calendar.date(year, month, day)
        self.assertIsNotNone(d)

    def check_invalid_date(self, year, month, day):
        self.assertRaises(Exception, lambda : self.calendar(year, month, day))

    def test_leap_year_from_before_1582(self):
        """Pope Gregory introduced the calendar in 1582"""
        self.check_valid_date(1200, 2, 29)

    def test_day_missed_out_in_British_calendar_change(self):
        """This date never happened in English law:
           It was missed when changing from the Julian to
           Gregorian. This test proves that we are not
           using a historical British calendar."""
        self.check_valid_date(1752, 9, 3)

    def test_Julian_leap_day_is_not_a_valid_date(self):
        """This day /was/ a leap day contemporaneously,
           but is not a valid date of the Gregorian calendar."""
        self.check_invalid_date(1300, 2, 29)

