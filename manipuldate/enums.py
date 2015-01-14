from enum import Enum


class DaysOfWeek(Enum):
    """ Enumeration that holds the days of the week and their "index".  """

    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6


class DateTimeDefaults(Enum):
    """ Enumeration that holds basic information regarding the amount of
    X IN Y. """

    Years_In_Century = 100
    Years_In_Decade = 10
    Months_In_Year = 12
    Weeks_In_Year = 52
    Days_In_Year = 365
    Days_In_Week = 7
    Hours_In_Day = 24
    Minutes_In_Hour = 60
    Seconds_In_Minutes = 60