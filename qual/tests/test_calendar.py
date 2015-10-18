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

class JulianGregorianConversion(unittest.TestCase):
    def setUp(self):
        self.gregorian = qual.ProlepticGregorianCalendar()
        self.julian = qual.JulianCalendar()
        self.addTypeEqualityFunc(
            qual.DateWithCalendar,
            qual.DateWithCalendar.make_assertEqual(self)
        )

    def Julian_to_Gregorian_conversion(self, julian_args, gregorian_args):
        julian_date = self.julian.date(*julian_args)
        gregorian_date = self.gregorian.date(*gregorian_args)
        converted_date = julian_date.convert_to(self.gregorian)
        self.assertEqual(
            converted_date,
            gregorian_date,
        )

    def Gregorian_to_Julian_conversion(self, julian_args, gregorian_args):
        gregorian_date = self.gregorian.date(*gregorian_args)
        julian_date = self.julian.date(*julian_args)
        converted_date = gregorian_date.convert_to(self.julian)
        self.assertEqual(
            converted_date,
            julian_date,
        )

    def check_both_conversions(self, julian_args, gregorian_args):
        self.Julian_to_Gregorian_conversion(julian_args, gregorian_args)
        self.Gregorian_to_Julian_conversion(julian_args, gregorian_args)

    def test_first_day_of_Gregorian_calendar(self):
        """ This date is the first day the Gregorian calendar was used
            in Catholic countries which adopted the new calendar immediately.
            We should be able to convert it from Julian to Gregorian."""
        self.check_both_conversions(
            (1582, 10, 5),
            (1582, 10, 15)
        )

    def test_a_Julian_only_leap_day(self):
        """ This date is a leap day of the Julian calendar.
            The corresponding day of the Gregorian calendar is not a leap day,
            and that year is not leap in the Gregorian calendar. """
        self.check_both_conversions(
            (1500, 2, 29),
            (1500, 3, 10)
        )

    def test_another_Julian_only_leap_day(self):
        """ This date is a leap day of the Julian calendar.
            The corresponding day of the Gregorian calendar is not a leap day,
            and that year is not leap in the Gregorian calendar. """
        self.check_both_conversions(
            (1400, 2, 29),
            (1400, 3, 9)
        )

    def test_a_Gregorian_March_1st(self):
        """ This Gregorian date is March 1st, of a Julian-only leap year.
            Although the Julian date falls before the leap day,
            since the Gregorian date falls after it, the number of 
            days difference between the dates in the two calendars
            depends which calendar you use to measure it. """
        self.check_both_conversions(
            (1500, 2, 20),
            (1500, 3, 1)
        )

