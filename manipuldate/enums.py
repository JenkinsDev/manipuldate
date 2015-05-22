from enum import Enum


class DaysOfWeek(Enum):
    """ Enumeration that holds the days of the week and their "index".
    """

    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6


class DateTimeDefaults(Enum):
    """ Enumeration that holds basic information regarding the amount of
    X IN Y.
    """

    Years_In_Century = 100
    Years_In_Decade = 10
    Months_In_Year = 12
    Weeks_In_Year = 52
    Days_In_Year = 365
    Days_In_Week = 7
    Hours_In_Day = 24
    Minutes_In_Hour = 60
    Seconds_In_Minutes = 60


class Months(Enum):
    """ Enumeration that holds month data.
    """

    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    Novemeber = 11
    December = 12


class DateTimeFormats(Enum):
    """ Enumeration that holds popular datetime formats.
    """

    Atom = "%Y-%m-%dT%H:%M:%S%z"
    W3C = "%Y-%m-%dT%H:%M:%S%z"
    RFC3339 = "%Y-%m-%dT%H:%M:%S%z"
    Cookie = "%a, %d %b %Y %H:%M:%S"