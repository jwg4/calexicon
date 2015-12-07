import unittest

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
