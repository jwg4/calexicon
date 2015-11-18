from datetime import date, timedelta

class InvalidDate(Exception):
    pass

class DateWithCalendar(date):
    def __init__(self, calendar_class, d):
        self.calendar = calendar_class
        date.__init__(self, d.year, d.month. d.day)

    def convert_to(self, calendar):
        return calendar.from_date(self)

    def __eq__(self, other):
        if super(DateWithCalendar, self) != super(DateWithCalendar, other):
            return False
        return self.calendar == other.calendar

    def __str__(self):
        return "%s (%s)" % (self.calendar.date_display_string(self), self.calendar.display_name)

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

