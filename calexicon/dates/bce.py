from base import BasicBCEDate
from ..helpers import ordinal, month_string
from ..constants import first_julian_date


class BCEDate(BasicBCEDate):
    def __str__(self):
        date_string = "%s %s %s BCE" % (
            ordinal(self.day),
            month_string(self.month),
            -self.year
        )
        display_name = (
            "Julian Calendar"
            if (self >= first_julian_date)
            else "Proleptic Julian Calendar"
        )
        return "%s (%s)" % (date_string, display_name)

    def __ge__(self, other):
        if self.year != other.year:
            return self.year > other.year
        if self.month != other.month:
            return self.month > other.month
        return self.day >= other.day
