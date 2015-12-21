import unittest 

from datetime import date as vanilla_date, timedelta

from calexicon.dates import DistantDate

class TestDistantDate(unittest.TestCase):
    def test_subtraction(self):
        dd = DistantDate(10000, 1, 1)
        self.assertIsInstance(dd - vanilla_date(9999, 1, 1), timedelta)
        self.assertIsInstance(dd - timedelta(0), DistantDate)

    def test_subtract_correct_result(self):
        dd = DistantDate(10000, 1, 2)
        dd2 = DistantDate(10000, 1, 1)
        self.assertEqual(dd - dd2, timedelta(days=1))
