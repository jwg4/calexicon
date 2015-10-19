from datetime import date

from base import Calendar
from main import JulianCalendar

class JulianToGregorianCalendar(Calendar):
    def date(self, year, month, day):
        gregorian_date = date(year, month, day)
        if gregorian_date < self.first_gregorian_day:
            return JulianCalendar().date(year, month, day)
        return self.from_date(gregorian_date)

class EnglishHistoricalCalendar(JulianToGregorianCalendar):
    first_gregorian_day = date(1752, 9, 14)
