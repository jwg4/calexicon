import unittest

from datetime import date, timedelta

from calexicon.dates import DateWithCalendar


class TestDateWithCalendar(unittest.TestCase):
    def setUp(self):
        date_dt = date(2010, 8, 1)
        self.date_wc = DateWithCalendar(None, date_dt)

    def test_comparisons(self): 
        self.assertTrue(self.date_wc < date(2010, 8, 2))
        self.assertFalse(self.date_wc < date(2010, 7, 31))
        self.assertTrue(self.date_wc > date(2010, 7, 2))
        self.assertFalse(self.date_wc > date(2010, 8, 31))

    def test_nonstrict_comparisons(self): 
        self.assertTrue(self.date_wc <= date(2010, 8, 2))
        self.assertFalse(self.date_wc <= date(2010, 7, 31))
        self.assertTrue(self.date_wc >= date(2010, 7, 2))
        self.assertFalse(self.date_wc >= date(2010, 8, 31))
        self.assertTrue(self.date_wc <= date(2010, 8, 1))
        self.assertTrue(self.date_wc >= date(2010, 8, 1))

    def test_subtraction(self):
        self.assertEqual(self.date_wc - date(2012, 10, 30), timedelta(days=-821))
