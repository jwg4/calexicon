import unittest

from calexicon.internal.julian import distant_julian_to_gregorian

class TestJulian(unittest.TestCase):
    def test_distant_julian_to_gregorian(self):
        self.assertEqual(distant_julian_to_gregorian(9999, 12, 1), (10000, 2, 12))
        
