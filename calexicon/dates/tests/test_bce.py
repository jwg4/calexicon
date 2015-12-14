import unittest

from datetime import timedelta

from calexicon.dates import BCEDate


class TestBCEDate(unittest.TestCase):

    def test_make_bce_date(self):
        bd = BCEDate(-4713, 1, 1)
        self.assertEqual(bd.julian_representation(), (-4713, 1, 1))

    def test_equality(self):
        self.assertEqual(BCEDate(-44, 3, 15), BCEDate(-44, 3, 15))

    def test_subtraction(self):
        self.assertEqual(timedelta(days=4), BCEDate(-44, 3, 15) - BCEDate(-44, 3, 11))
        self.assertEqual(timedelta(days=33), BCEDate(-44, 3, 15) - BCEDate(-44, 2, 11))
