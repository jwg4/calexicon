import sys

if sys.hexversion < 0x02070000:
    import unittest2 as unittest
else:
    import unittest
from datetime import date as vanilla_date

from hypothesis import given, example
from hypothesis.strategies import integers
from hypothesis.extra.datetime import datetimes

from .calendar_testing import CalendarTest

from calexicon.calendars.main import JulianCalendar, ProlepticJulianCalendar, ProlepticGregorianCalendar
from calexicon.calendars.other import JulianDayNumber, AstronomicalCalendar
from calexicon.constants import julian_day_number_of_last_vanilla_date, last_vanilla_year
from calexicon.dates import BCEDate, DateWithCalendar, DistantDate


class TestJulianDayNumber(CalendarTest):
    def setUp(self):
        self.calendar = JulianDayNumber()
        self.setUpDateEquality()

    def test_make_date(self):
        vd = vanilla_date(2010, 8, 1)
        d = self.calendar.from_date(vd)
        self.assertIsNotNone(d)

    def test_first_date(self):
        vd = vanilla_date(1, 1, 1)
        d = self.calendar.from_date(vd)
        self.assertEqual(str(d), 'Day 1721423 (Julian Day Number)')

    def test_make_bce_date(self):
        bd = BCEDate(-4713, 1, 1)
        d = self.calendar.from_date(bd)
        self.assertIsNotNone(d)
        self.assertEqual(d.to_date(), bd)

    def test_make_bce_date_check_calendar(self):
        bd = BCEDate(-4713, 1, 1)
        d = self.calendar.from_date(bd)
        self.assertEqual(d.calendar, self.calendar.__class__)

    def compare_date_and_number(self, year, month, day, number):
        vd = vanilla_date(year, month, day)
        d = self.calendar.from_date(vd)
        self.assertEqual(d.native_representation(), {'day_number': number})

    def test_every_400_years(self):
        days_in_400_years = 400 * 365 + 97
        for i in range(25):
            self.compare_date_and_number(1 + 400 * i, 1, 1, 1721423 + days_in_400_years * i)

    def test_first_jan_2000s(self):
        first_jan_2001 = 2451908
        self.compare_date_and_number(2001, 1, 1, first_jan_2001)
        self.compare_date_and_number(2002, 1, 1, first_jan_2001 + 365)
        self.compare_date_and_number(2003, 1, 1, first_jan_2001 + 365 * 2)
        self.compare_date_and_number(2004, 1, 1, first_jan_2001 + 365 * 3)
        self.compare_date_and_number(2005, 1, 1, first_jan_2001 + 365 * 4 + 1)
        self.compare_date_and_number(2006, 1, 1, first_jan_2001 + 365 * 5 + 1)
        self.compare_date_and_number(2007, 1, 1, first_jan_2001 + 365 * 6 + 1)
        self.compare_date_and_number(2008, 1, 1, first_jan_2001 + 365 * 7 + 1)
        self.compare_date_and_number(2009, 1, 1, first_jan_2001 + 365 * 8 + 2)
        self.compare_date_and_number(2010, 1, 1, first_jan_2001 + 365 * 9 + 2)
        self.compare_date_and_number(2011, 1, 1, first_jan_2001 + 365 * 10 + 2)
        self.compare_date_and_number(2012, 1, 1, first_jan_2001 + 365 * 11 + 2)
        self.compare_date_and_number(2013, 1, 1, first_jan_2001 + 365 * 12 + 3)

    def test_another_date(self):
        self.compare_date_and_number(2013, 1, 1, 2456291)

    @given(integers(max_value=julian_day_number_of_last_vanilla_date))
    def test_construct_from_day_number(self, x):
        d = self.calendar.date(x)
        self.assertIsNotNone(d)

    @given(integers(max_value=julian_day_number_of_last_vanilla_date))
    def test_constructed_date_has_right_calendar(self, x):
        d = self.calendar.date(x)
        self.assertEqual(d.calendar, self.calendar.__class__)

    def test_construct_from_specific_day_number(self):
        d = self.calendar.date(0)
        self.assertEqual(d, self.calendar.from_date(BCEDate(-4713, 1, 1)))

    @example(-998278577)
    @given(integers(max_value=julian_day_number_of_last_vanilla_date))
    def test_round_trip_from_day_number(self, x):
        d = self.calendar.date(x)
        rep = d.native_representation()
        self.assertTrue('day_number' in rep)

    @given(datetimes(timezones=[]))
    def test_round_trip_from_date(self, dt):
        vd = dt.date()
        d = self.calendar.from_date(vd)
        dn = d.native_representation()['day_number']
        new_d = self.calendar.date(dn)
        self.assertEqual(d, new_d)


class TestJulianDateConversion(unittest.TestCase):
    def setUp(self):
        self.addTypeEqualityFunc(
            DateWithCalendar,
            DateWithCalendar.make_assertEqual(self)
        )

    def test_conversion(self):
        calendar = ProlepticJulianCalendar()
        d = calendar.date(9999, 12, 1)
        converted = d.convert_to(JulianDayNumber())
        self.assertIsNotNone(converted)
        expected = DateWithCalendar(JulianDayNumber, DistantDate(10000, 2, 12))
        self.assertEqual(converted, expected)

    def test_conversion_2(self):
        calendar = ProlepticJulianCalendar()
        d = calendar.date(9999, 9, 19)
        converted = d.convert_to(JulianDayNumber())
        self.assertIsNotNone(converted)
        expected = DateWithCalendar(JulianDayNumber, vanilla_date(9999, 12, 1))
        self.assertEqual(converted, expected)

    def test_jdn_to_julian(self):
        calendar = JulianDayNumber()
        d = calendar.date(5373524)
        converted = d.convert_to(ProlepticJulianCalendar())
        self.assertIsNotNone(converted)
        expected = DateWithCalendar(ProlepticJulianCalendar, DistantDate(10000, 2, 12))
        self.assertEqual(converted, expected)


class TestAstronomicalCalendar(CalendarTest):
    def setUp(self):
        self.calendar = AstronomicalCalendar()
        self.addTypeEqualityFunc(
            DateWithCalendar,
            DateWithCalendar.make_assertEqual(self)
        )

    def test_zero_year_date(self):
        d = self.calendar.date(0, 1, 1)
        self.assertIsNotNone(d)

    def test_non_zero_year_date(self):
        d = self.calendar.date(1, 1, 1)
        self.assertIsNotNone(d)

    @given(integers(min_value=1583, max_value=last_vanilla_year))
    def test_CE_dates_after_1582(self, y):
        d = self.calendar.date(y, 1, 1)
        converted = d.convert_to(ProlepticGregorianCalendar())
        self.assertIsNotNone(converted)
        expected = ProlepticGregorianCalendar().date(y, 1, 1)
        self.assertEqual(converted, expected)

    @given(integers(min_value=1, max_value=1582))
    def test_CE_dates_before_1582(self, y):
        d = self.calendar.date(y, 1, 1)
        converted = d.convert_to(JulianCalendar())
        self.assertIsNotNone(converted)
        expected = ProlepticJulianCalendar().date(y, 1, 1)
        self.assertEqual(converted, expected)

    @example(-2147483648)
    @given(integers(max_value=-45))
    def test_BCE_proleptic_dates(self, y):
        expected = ProlepticJulianCalendar().date(y-1, 1, 1)
        d = self.calendar.date(y, 1, 1)
        converted = d.convert_to(ProlepticJulianCalendar())
        self.assertIsNotNone(converted)
        self.assertEqual(converted, expected)

    @given(integers(min_value=-44, max_value=-1))
    def test_BCE_julian_dates(self, y):
        expected = JulianCalendar().date(y-1, 1, 1)
        d = self.calendar.date(y, 1, 1)
        converted = d.convert_to(JulianCalendar())
        self.assertIsNotNone(converted)
        self.assertEqual(converted, expected)
