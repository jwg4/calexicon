from datetime import date, timedelta

class DateWithCalendar(object):
    def __init__(self, calendar_class, date):
        self.calendar = calendar_class
        self.date = date

    def convert_to(self, calendar):
        return calendar.from_date(self.date)

    def __eq__(self, other):
        return self.calendar == other.calendar and self.date == other.date

class Calendar(object):
    def from_date(self, date):
        return DateWithCalendar(self.__class__, date)

class ProlepticGregorianCalendar(Calendar):
    def date(self, year, month, day):
        d = date(year, month, day)
        return self.from_date(d)

class JulianCalendar(Calendar):
    def date(self, year, month, day):
        d = date(year, month, day)
        d = d + timedelta(days=10)
        return self.from_date(d)

