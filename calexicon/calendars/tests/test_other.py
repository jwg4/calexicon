from datetime import date as vanilla_date

from calendar_testing import CalendarTest

from calexicon.calendars.other import JulianDayNumber

class TestJulianDayNumber(CalendarTest):
    def setUp(self):
        self.calendar = JulianDayNumber()

    def test_make_date(self):
        vd = vanilla_date(2010, 8, 1)
        d = self.calendar.from_date(vd)
        self.assertIsNotNone(d)

    def test_first_date(self):
        vd = vanilla_date(1, 1, 1)
        d = self.calendar.from_date(vd)
        self.assertEqual(str(d), 'Day 1721423 (Julian Day Number)')

    def compare_date_and_number(self, year, month, day, number):
        vd = vanilla_date(year, month, day)
        d = self.calendar.from_date(vd)
        self.assertEqual(d.native_representation(), {'day_number': number})

    def test_every_400_years(self):
        days_in_400_years = 400 * 365 + 97
        for i in range(25):
            self.compare_date_and_number(1 + 400 * i, 1, 1, 1721423 + days_in_400_years * i)

    def test_another_date(self):
        self.compare_date_and_number(2013, 1, 1, 2456293)
