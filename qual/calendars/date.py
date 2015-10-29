from datetime import date, timedelta

class InvalidDate(Exception):
    pass

class DateWithCalendar(object):
    def __init__(self, calendar_class, date):
        self.calendar = calendar_class
        self.date = date

    def convert_to(self, calendar):
        return calendar.from_date(self.date)

    def __eq__(self, other):
        return self.calendar == other.calendar and self.date == other.date

    def __str__(self):
        return "%s (%s)" % (self.date, self.calendar.display_name)

    def __lt__(self, other):
        other_date = other
        if isinstance(other, DateWithCalendar):
            other_date = other.date
        return self.date < other_date

    def __gt__(self, other):
        other_date = other
        if isinstance(other, DateWithCalendar):
            other_date = other.date
        return self.date > other_date

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

