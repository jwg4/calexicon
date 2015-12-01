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

    def test_first_jan_2000s(self):
        first_jan_2001 = 2451908
        self.compare_date_and_number(2001, 1, 1, first_jan_2001)
        self.compare_date_and_number(2002, 1, 1, first_jan_2001 + 365)
        self.compare_date_and_number(2003, 1, 1, first_jan_2001 + 365 * 2)
        self.compare_date_and_number(2004, 1, 1, first_jan_2001 + 365 * 3)
        self.compare_date_and_number(2005, 1, 1, first_jan_2001 + 365 * 4 + 1)
        self.compare_date_and_number(2006, 1, 1, first_jan_2001 + 365 * 5 + 1)
        self.compare_date_and_number(2007, 1, 1, first_jan_2001 + 365 * 6 + 1)
        self.compare_date_and_number(2008, 1, 1, first_jan_2001 + 365 * 7 + 1)
        self.compare_date_and_number(2009, 1, 1, first_jan_2001 + 365 * 8 + 2)
        self.compare_date_and_number(2010, 1, 1, first_jan_2001 + 365 * 9 + 2)
        self.compare_date_and_number(2011, 1, 1, first_jan_2001 + 365 * 10 + 2)
        self.compare_date_and_number(2012, 1, 1, first_jan_2001 + 365 * 11 + 2)
        self.compare_date_and_number(2013, 1, 1, first_jan_2001 + 365 * 12 + 3)

    def test_another_date(self):
        self.compare_date_and_number(2013, 1, 1, 2456293)
