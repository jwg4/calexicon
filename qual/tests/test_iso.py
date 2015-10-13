import unittest

import qual

from datetime import date

class TestIsoUtils(unittest.TestCase):
    def test_round_trip_date(self):
        d = date(2010, 8, 1)
        self.assertEqual(qual.iso_to_gregorian(*d.isocalendar()), d)

