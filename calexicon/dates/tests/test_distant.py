import unittest 

from datetime import date as vanilla_date, timedelta

from calexicon.calendars import ProlepticJulianCalendar
from calexicon.dates import DateWithCalendar, DistantDate

class TestDistantDate(unittest.TestCase):
    def test_subtraction(self):
        dd = DistantDate(10000, 1, 1)
        self.assertIsInstance(dd - vanilla_date(9999, 1, 1), timedelta)
        self.assertIsInstance(dd - timedelta(0), DistantDate)

    def test_subtract_correct_result(self):
        dd = DistantDate(10000, 1, 2)
        dd2 = DistantDate(10000, 1, 1)
        self.assertEqual(dd - dd2, timedelta(days=1))

    def test_subtract_vanilla_date_from_distant_date(self):
        dd = DistantDate(10000, 1, 2)
        d = vanilla_date(9984, 2, 29)
        x = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 15 * 365 + 3 + 2
        self.assertEqual(dd - d, timedelta(days=x))

    def test_subtract_early_vanilla_date(self):
        dd = DistantDate(10000, 2, 12)
        d = vanilla_date(1, 1, 1)
        x = vanilla_date(9999, 12, 31) - vanilla_date(1, 1, 1) + timedelta(days=43)
        self.assertEqual(dd - d, x)

    def test_subtract_two_distant_dates(self):
        dd = DistantDate(10000, 2, 12)
        dd2 = DistantDate(10000, 1, 1)
        self.assertEqual(dd - dd2, timedelta(days=42))

    def test_subtract_timedelta_from_dd(self):
        dd = DistantDate(10000, 2, 12)
        td = timedelta(days=1)
        self.assertEqual(dd - td, DistantDate(10000, 2, 11))

    def test_addition(self):
        dd = DistantDate(10000, 1, 1)
        td = timedelta(days=1)
        self.assertEqual(dd + td, DistantDate(10000, 1, 2))

    def test_equality(self):
        dd = DistantDate(2010, 8, 1)
        ProlepticJulianCalendar().bless(dd)
        dwc = DateWithCalendar(ProlepticJulianCalendar, DistantDate(2010, 8, 1)) 
        self.assertTrue(dwc == dd)

    def test_equality_2(self):
        dd = DistantDate(2010, 8, 1)
        ProlepticJulianCalendar().bless(dd)
        dwc = DateWithCalendar(ProlepticJulianCalendar, DistantDate(2010, 8, 1)) 
        self.assertTrue(dd == dwc)

    def test_equality_of_two_distant_dates(self):
        d1 = DistantDate(2010, 8, 1)
        d2 = DistantDate(2010, 8, 1)
        self.assertTrue(d1 == d2)

    def test_julian_to_gregorian(self):
        self.assertEqual(DistantDate.julian_to_gregorian(9999, 12, 1), (10000, 2, 12))
