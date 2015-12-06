from ..calendars import JulianCalendar, ProlepticGregorianCalendar


def julian_to_gregorian(year, month, day):
    calendar = JulianCalendar()
    d = calendar.date(year, month, day)
    converted = d.convert_to(ProlepticGregorianCalendar())
    converted = converted.native_representation()
    return (converted['year'], converted['month'], converted['day'])


def gregorian_to_julian(year, month, day):
    calendar = ProlepticGregorianCalendar()
    d = calendar.date(year, month, day)
    converted = d.convert_to(JulianCalendar()).native_representation()
    return (converted['year'], converted['month'], converted['day'])
