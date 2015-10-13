import unittest
from hypothesis import given
from hypothesis.extra.datetime import datetimes

import qual

from datetime import date

class TestIsoUtils(unittest.TestCase):
    @given(datetimes())
    def test_round_trip_date(self, dt):
        d = dt.date()
        self.assertEqual(qual.iso_to_gregorian(*d.isocalendar()), d)

