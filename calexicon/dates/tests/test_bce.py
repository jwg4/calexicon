import unittest

from calexicon.dates import BCEDate


class TestBCEDate(unittest.TestCase):

    def test_make_bce_date(self):
        bd = BCEDate(-4713, 1, 1)
        self.assertEqual(bd.julian_representation(), (-4713, 1, 1))

    def test_equality(self):
        self.assertEqual(BCEDate(-44, 3, 15), BCEDate(-44, 3, 15))
