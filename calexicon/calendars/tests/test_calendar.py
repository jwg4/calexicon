import sys

if sys.hexversion < 0x02070000:
    import unittest2 as unittest
else:
    import unittest

from hypothesis import given, example, assume
from hypothesis.strategies import integers
from hypothesis.extra.datetime import datetimes

from datetime import date, datetime

from calexicon.calendars import DateWithCalendar, ProlepticGregorianCalendar, JulianCalendar, InvalidDate, ProlepticJulianCalendar
from calendar_testing import CalendarTest

class TestProlepticGregorianCalendar(CalendarTest):
    def setUp(self):
        self.calendar = ProlepticGregorianCalendar()

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
        self.assertEqual(d.calendar, ProlepticGregorianCalendar)

    def test_display_string(self):
        """ The display string for a date gives the correct date and specifies the calendar. """
        d = self.calendar.date(1415, 11, 3)
        self.assertEqual(str(d), "3rd November 1415 (Proleptic Gregorian Calendar)")

class TestJulianCalendar(CalendarTest):
    def setUp(self):
        self.calendar = JulianCalendar()
        self.addTypeEqualityFunc(
            DateWithCalendar,
            DateWithCalendar.make_assertEqual(self)
        )

    def test_display_string(self):
        """ The display string for a date gives the correct date and specifies the calendar. """
        d = self.calendar.date(1415, 10, 25)
        self.assertEqual(str(d), "25th October 1415 (Julian Calendar)")

    @given(datetimes(timezones=[]))
    @example(datetime(2100, 3, 1, 0, 0, 0))
    @example(datetime(4500, 4, 1, 0, 0, 0))
    @example(datetime(8200, 3, 1, 0, 0, 0))
    def test_make_julian_date_directly_and_via_year_month_day(self, dt):
        d = dt.date()
        julian_date_from_date = self.calendar.from_date(d)
        julian_representation = self.calendar.julian_representation(d)
        year, month, day = julian_representation
        julian_date_from_representation = self.calendar.date(year, month, day)
        self.assertEqual(julian_date_from_date, julian_date_from_representation)

    def test_julian_number(self):
        d = self.calendar.date(1415, 10, 25)
        self.assertEqual(self.calendar.julian_day_number(d), 2238184)

class TestProlepticJulianCalendar(TestJulianCalendar):
    def setUp(self):
        self.calendar = ProlepticJulianCalendar()
        self.addTypeEqualityFunc(
            DateWithCalendar,
            DateWithCalendar.make_assertEqual(self)
        )

    def test_year_1_bce(self):
        self.check_valid_date(-1, 3, 1)

    @given(integers(1, 12), integers(1, 31))
    def test_year_0_does_not_exist(self, month, day):
        self.check_invalid_date(0, month, day)

    @given(integers(None, -1))
    def test_feb_29th_does_not_exist_except_julian_leap_years(self, year):
        assume(year % 4 != 0)
        self.check_invalid_date(year, 2, 29)

    @given(integers(None, -1))
    def test_feb_29th_does_exist_in_julian_leap_years(self, year):
        assume(year % 4 == 0)
        self.check_valid_date(year, 2, 29)

    def test_display_string_for_bce_date(self):
        """ The display string for a date gives the correct date and specifies the calendar. """
        d = self.calendar.date(-44, 3, 15)
        self.assertEqual(str(d), "15th March 44 BCE (Julian Calendar)")

    def test_display_string_for_proleptic_date(self):
        """ The display string for a date gives the correct date and specifies the calendar. """
        d = self.calendar.date(-100, 7, 13)
        self.assertEqual(str(d), "13th July 100 BCE (Proleptic Julian Calendar)")

class TestBCEDate(unittest.TestCase):
    def test_greater_than(self):
        self.assertFalse(
            ProlepticJulianCalendar.BCEDate(-100, 7, 13) >= 
            ProlepticJulianCalendar.BCEDate(-45, 1, 1)
        )

class JulianGregorianConversion(unittest.TestCase):
    def setUp(self):
        self.gregorian = ProlepticGregorianCalendar()
        self.julian = JulianCalendar()
        self.addTypeEqualityFunc(
            DateWithCalendar,
            DateWithCalendar.make_assertEqual(self)
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

    def test_the_day_before_a_Julian_only_leap_day(self):
        """ This date is Feb 28th before leap day of the Julian calendar.
            The corresponding day of the Gregorian calendar is not a leap day,
            and that year is not leap in the Gregorian calendar. """
        self.check_both_conversions(
            (1500, 2, 28),
            (1500, 3, 9)
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

    def test_a_Gregorian_Feb_28th(self):
        """ This Gregorian date is Feb 28th, of a Julian-only leap year.
            Both the Gregorian date, and the Julian date, are unaffected
            by the Julian leap day later in that year."""
        self.check_both_conversions(
            (1500, 2, 19),
            (1500, 2, 28)
        )

    @given(datetimes(timezones=[]))
    @example(datetime(8200, 3, 1, 0, 0, 0))
    @example(datetime(8200, 2, 28, 0, 0, 0))
    @example(datetime(8199, 12, 31, 0, 0, 0))
    def test_round_trip_Gregorian_Julian_Gregorian(self, dt):
        original_gregorian_date = self.gregorian.from_date(dt.date())
        converted_date = original_gregorian_date.convert_to(self.julian)
        round_tripped_date = converted_date.convert_to(self.gregorian)
        self.assertEqual(original_gregorian_date, round_tripped_date)
    
    @given(datetimes(timezones=[]))
    @example(datetime(8200, 3, 1, 0, 0, 0))
    @example(datetime(8200, 2, 28, 0, 0, 0))
    @example(datetime(8199, 12, 31, 0, 0, 0))
    def test_round_trip_Julian_Gregorian_Julian(self, dt):
        original_julian_date = self.julian.from_date(dt.date())
        converted_date = original_julian_date.convert_to(self.gregorian)
        round_tripped_date = converted_date.convert_to(self.julian)
        self.assertEqual(original_julian_date, round_tripped_date)


