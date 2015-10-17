import unittest

from datetime import date

import qual

class TestProlepticGregorianCalendar(unittest.TestCase):
    def setUp(self):
        self.calendar = qual.ProlepticGregorianCalendar()

    def test_valid_date(self):
        d = self.calendar.date(1200, 2, 29)
        self.assertIsNotNone(d)

