from datetime import date, timedelta

from date import DateWithCalendar

class Calendar(object):
    def from_date(self, date):
        return DateWithCalendar(self.__class__, date)

