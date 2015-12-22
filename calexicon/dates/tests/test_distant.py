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

    def test_equality(self):
        dd = DistantDate(2010, 8, 1)
        ProlepticJulianCalendar().bless(dd)
        dwc = DateWithCalendar(ProlepticJulianCalendar, DistantDate(2010, 8, 1)) 
        self.assertTrue(dwc == dd)
