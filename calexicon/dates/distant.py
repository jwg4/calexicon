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

    def __ge__(self, other):
        if self.year != other.year:
            return self.year > other.year
        if self.month != other.month:
            return self.month > other.month
        return self.day >= other.day

    def __le__(self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return not (self >= other)

    def __lt__(self, other):
        return not (self >= other)

    def __gt__(self, other):
        return not (self <= other)
