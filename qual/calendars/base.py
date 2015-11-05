from datetime import date, timedelta

from dates import DateWithCalendar

class Calendar(object):
    def from_date(self, d):
        return DateWithCalendar(self.__class__, d)

