import unittest

from datetime import date, timedelta

from calexicon.dates import DateWithCalendar


class TestDateWithCalendar(unittest.TestCase):
    def setUp(self):
        date_dt = date(2010, 8, 1)
        self.date_wc = DateWithCalendar(None, date_dt)
        self.addTypeEqualityFunc(
            DateWithCalendar,
            DateWithCalendar.make_assertEqual(self)
        )

    def test_equality(self):
        self.assertTrue(self.date_wc != date(2010, 8, 1))

    def test_not_equal(self):
        """ Check that assertNotEqual works correctly.
            The main purpose of this test is to have code
            coverage for the false branch of the
            custom assertEqual. """
        try:
            self.assertEqual(self.date_wc, date(2010, 8, 1))
        except AssertionError:
            pass

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
