from datetime import date, timedelta

class InvalidDate(Exception):
    pass

class DateWithCalendar(object):
    def __init__(self, calendar_class, d):
        self.calendar = calendar_class
        self._date = d

    def convert_to(self, calendar):
        return calendar.from_date(self._date)

    def __eq__(self, other):
        return self.calendar == other.calendar and self._date == other._date

    def __str__(self):
        return "%s (%s)" % (self.calendar.date_display_string(self._date), self.calendar.display_name)

    def __lt__(self, other):
        try:
            other_date = other._date
        except:
            other_date = other
        return self._date < other_date

    def __gt__(self, other):
        try:
            other_date = other._date
        except:
            other_date = other
        return self._date > other_date

    def __le__(self, other):
        try:
            other_date = other._date
        except:
            other_date = other
        return self._date <= other_date

    def __ge__(self, other):
        try:
            other_date = other._date
        except:
            other_date = other
        return self._date >= other_date

    def __sub__(self, other):
        try:
            other_date = other._date
        except:
            other_date = other
        return self._date - other_date

    @staticmethod
    def make_assertEqual(test_case):
        def assertEqual(a, b, msg):
            if a.__eq__(b):
                return True
            else:
                if msg is None:
                    msg = "%s is not equal to %s" % (a, b)
                raise test_case.failureException(msg)
        return assertEqual

