import sys
if sys.hexversion < 0x02070000:
    import unittest2 as unittest
else:
    import unittest

from hypothesis import given, example
from hypothesis.extra.datetime import datetimes

from datetime import date as vanilla_date, datetime

from calexicon.calendars.tests.test_calendar import JulianGregorianConversion

from calexicon.fn import julian_to_gregorian, gregorian_to_julian
from calexicon.fn import julian_to_julian_day_number, julian_day_number_to_julian


class TestJulianConversion(JulianGregorianConversion):
    def setUp(self):
        pass

    def Julian_to_Gregorian_conversion(self, julian_args, gregorian_args):
        result = julian_to_gregorian(*julian_args)
        self.assertEqual(
            result,
            gregorian_args,
        )

    def Gregorian_to_Julian_conversion(self, julian_args, gregorian_args):
        result = gregorian_to_julian(*gregorian_args)
        self.assertEqual(
            result,
            julian_args,
        )


class TestJulianNumberConversion(unittest.TestCase):
    def test_number_to_julian_date(self):
        self.assertEqual(julian_to_julian_day_number(-4713, 1, 1), 0)
        self.assertEqual(julian_to_julian_day_number(-4712, 1, 1), 365)

    def test_julian_date_to_number(self):
        self.assertEqual(julian_day_number_to_julian(0), (-4713, 1, 1))
        self.assertEqual(julian_day_number_to_julian(365), (-4712, 1, 1))

    @example(datetime(9999, 12, 1, 0, 0, 0))
    @given(datetimes(timezones=[]))
    def test_round_trip_from_date_compare_tuples(self, dt):
        vd = dt.date()
        (y, m, d) = (vd.year, vd.month, vd.day)
        jdn = julian_to_julian_day_number(y, m, d)
        result = julian_day_number_to_julian(jdn)
        self.assertEqual(result, (y, m, d))

    @given(datetimes(timezones=[]))
    def test_round_trip_from_date_compare_vanilla_dates(self, dt):
        vd = dt.date()
        (y, m, d) = (vd.year, vd.month, vd.day)
        jdn = julian_to_julian_day_number(y, m, d)
        result = julian_day_number_to_julian(jdn)
        self.assertEqual(vd, vanilla_date(*result))
