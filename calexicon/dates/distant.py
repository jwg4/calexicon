from datetime import timedelta

from base import DateWithCalendar

class DistantDate(DateWithCalendar):
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    @property
    def _date(self):
        return self

    def __sub__(self, other):
        return timedelta(days=0)
