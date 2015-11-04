from datetime import date, timedelta

from date import DateWithCalendar

class Calendar(object):
    def from_date(self, d):
        return DateWithCalendar(self.__class__, d)

