import sys

if sys.hexversion < 0x02070000:
    import unittest2 as unittest
else:
    import unittest

from datetime import date

import qual

class CalendarTest(unittest.TestCase):
    def check_valid_date(self, year, month, day):
        d = self.calendar.date(year, month, day)
        self.assertIsNotNone(d)

    def check_invalid_date(self, year, month, day):
        self.assertRaises(Exception, lambda : self.calendar(year, month, day))

class TestProlepticGregorianCalendar(CalendarTest):
    def setUp(self):
        self.calendar = qual.ProlepticGregorianCalendar()

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

    def test_calendar_reference(self):
        """Can we retrieve the calendar from the date"""
        d = self.calendar.date(2010, 8, 1)
        self.assertEqual(d.calendar, qual.ProlepticGregorianCalendar)

class TestJulianCalendar(CalendarTest):
    def setUp(self):
        self.calendar = qual.JulianCalendar()

    def test_Julian_to_Gregorian_conversion(self):
        d = self.calendar.date(1582, 10, 5)
        c = qual.ProlepticGregorianCalendar()
        d2 = c.date(1582, 10, 15)
        self.assertEqual(d.convert_to(c), d2)
