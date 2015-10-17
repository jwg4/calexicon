from datetime import date

class DateWithCalendar(object):
    def __init__(self, calendar_class, date):
        self.calendar = calendar_class
        self.date = date

class ProlepticGregorianCalendar(object):
    def date(self, year, month, day):
        d = date(year, month, day)
        return DateWithCalendar(ProlepticGregorianCalendar, d)

