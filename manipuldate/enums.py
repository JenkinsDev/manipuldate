from enum import Enum


class DaysOfWeek(Enum):
    """ Enumeration that holds the days of the week and their "index".  """

    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6

    def __str__(self):
        return self.name


class DateTimeDefaults(Enum):
    """ Enumeration that holds basic information regarding the amount of
    X IN Y. """

    YEARS_IN_CENTURY = 100
    YEARS_IN_DECADE = 10
    MONTHS_IN_YEAR = 12
    WEEKS_IN_YEAR = 52
    DAYS_IN_YEAR = 365
    DAYS_IN_WEEK = 7
    HOURS_IN_DAY = 24
    MINUTES_IN_HOURS = 60
    SECONDS_IN_MINUTE = 60
