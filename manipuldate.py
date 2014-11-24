import datetime


class Manipuldate(datetime.datetime):
    """ Easy date/time/datetime manipulation with Python3.x+ """

    DEFAULT_STRING_FORMAT = 'Y-m-d H:i:s'

    # Amount time/dates in (x)
    YEARS_IN_CENTURY = 100
    YEARS_IN_DECADE = 10
    MONTHS_IN_YEAR = 12
    WEEKS_IN_YEAR = 52
    DAYS_IN_YEAR = 365
    DAYS_IN_WEEK = 7
    HOURS_IN_DAY = 24
    MINUTES_IN_HOURS = 60
    SECONDS_IN_MINUTE = 60

    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

    DAYS_OF_WEEK = {
        SUNDAY: "Sunday",
        MONDAY: "Monday",
        TUESDAY: "Tuesday",
        WEDNESDAY: "Wednesday",
        THURSDAY: "Thursday",
        FRIDAY: "Friday",
        SATURDAY: "Saturday"
    }

    @staticmethod
    def from_datetime(dt):
        """ Creates an instance of Manipuldate based on a supplied datetime instance.

        Parameters:
            :param dt: Datetime instance that we will be using to create our instance.

        Returns:
            Manipuldate Instance
        """
        return Manipuldate(dt.year, dt.month, dt.day, dt.hour, dt.minute,
                           dt.second, dt.microsecond, dt.tzinfo)

    @staticmethod
    def from_date(d):
        """ Creates an instance of Manipuldate based on a supplied date instance.

        Parameters:
            :param d: Date instance that we will be using to create our new instance.

        Returns:
            Manipuldate Instance
        """
        return Manipuldate(d.year, d.month, d.day)

    @staticmethod
    def from_time(t):
        """ Creates an instance of Manipuldate based on the supplied time instance.

        Parameters:
            :param t: Time instance that we will be using to create our new isntance.

        Returns:
            Manipuldate Instance
        """
        # Year, month and day are required by the datetime class.
        return Manipuldate(1970, 1, 1, t.hour, t.minute, t.second, t.microsecond, t.tzinfo)

    def _copy_to_new_instance(self, year=None, month=None, day=None, hour=None, minute=None,
                      second=None, microsecond=None, tzinfo=None):
        """ Creates a new instance of Manipuldate based on the supplied information,
        if something is set to None or False then we will use the corresponding
        attributes value.

        Parameters:
            :param year: Numerical value that represents years
            :param month: Numerical value that represents months [1-12]
            :param day: Numerical value that represents days [1-(28-31)]
            :param hour: Numerical value that represents hours [0-24]
            :param minute: Numerical value that represents minutes [0-60]
            :param second: Numerical value that represents seconds [0-60]
            :param second: Numerical value that represents microseconds [0-1000000]
            :param tzinfo: TimeZone information

        Returns:
            Manipuldate Instance
        """
        year = year or self.year
        month = month or self.month
        day = day or self.day
        hour = hour or self.hour
        minute = minute or self.minute
        second = second or self.second
        microsecond = microsecond or self.microsecond
        tzinfo = tzinfo or self.tzinfo
        return Manipuldate(year, month, day, hour, minute, second, microsecond, tzinfo)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """                                                                                    """
    """                                 Date Arithmetic                                    """
    """                                                                                    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def add_years(self, years):
        """ Adds the amount of provided years to our datetime object then
        returns a new instance of Manipuldate because of how datetime works
        within python.

        Parameters:
            :param years: The number of years to add to the current date.

        Returns:
            Manipuldate Instance
        """
        return self._copy_to_new_instance(year=self.year + years)

    def sub_years(self, years):
        """ Subtracts the amount of provided years from our datetime object
        then returns a new instance of Manipuldate because of how datetime
        works within python, no editable properties.

        Parameters:
            :param years: The number of years to sub from the current date.

        Returns:
            Manipuldate Instance
        """
        return self._copy_to_new_instance(year=self.year - years)

    def add_months(self, months):
        """ Adds the amount of provided months to our datetime object
        then returns a new instance of Manipuldate because of how datetime
        works within python, no editable properties.

        Parameters:
            :param months: The number of months to add to the current date.

        Returns:
            Manipuldate Instance
        """
        month, year = self.month + months, self.year
        while month > 12:
            year += 1
            month -= 12
        return self._copy_to_new_instance(year=year, month=month)

    def sub_months(self, months):
        """ Subtracts the amount of provided months from our datetime object
        then returns a new instance of Manipuldate because of how datetime
        works within python, no editable properties.

        Parameters:
            :param months: The number of months to sub from the current date.

        Returns:
            Manipuldate Instance
        """
        month, year = self.month - months, self.year
        while month <= 0:
            year -= 1
            month += 12
        return self._copy_to_new_instance(year=year, month=month)

    def add_weeks(self, weeks):
        """ Adds n-weeks * 7 days to the current date.

        Parameters:
            :param weeks: N weeks to add to the current date.

        Returns:
            Manipuldate Instance
        """
        return self.add_days(self.DAYS_IN_WEEK * weeks)

    def sub_weeks(self, weeks):
        """ Subtracts n-weeks * 7 days form the current date.

        Parameters:
            :param weeks: N-weeks to subtract from the current date.
        """
        return self.sub_days(self.DAYS_IN_WEEK * weeks)

    def add_days(self, days):
        """ Adds the amount of provided days to our datetime object then
        returns a new instance of Manipuldate because of how datetime works
        within python, no editable properties.

        Parameters:
            :param days: The number of months to add to the current date.

        Returns:
            Manipuldate Instance
        """
        return Manipuldate.from_datetime(self + datetime.timedelta(days=days))

    def sub_days(self, days):
        """ Subtracts the amount of provided days from our datetime object then
        returns a new instance of Manipuldate because of how datetime works
        within python, no editable properties.

        Parameters:
            :param days: The number of months to subtract from the current date.

        Returns:
            Manipuldate Instance
        """
        return Manipuldate.from_datetime(self - datetime.timedelta(days=days))

    ########################## DATE ARITHMETIC CONVENIENCE METHODS ##########################

    def add_year(self):
        """ Convenience method for adding one year.

        Returns:
            Manipuldate Instance
        """
        return self.add_years(1)

    def next_year(self):
        """ Convenience method for adding one year.

        Returns:
            Manipuldate Instance
        """
        return self.add_year()

    def sub_year(self):
        """ Convenience method for subtracting one year.

        Returns:
            Manipuldate Instance
        """
        return self.sub_years(1)

    def last_year(self):
        """ Convenience method for subtracting one year.

        Returns:
            Manipuldate Instance
        """
        return self.sub_year()

    def add_month(self):
        """ Convenience method for adding one month.

        Returns:
            Manipuldate Instance
        """
        return self.add_months(months=1)

    def next_month(self):
        """ Convenience method for adding one month.

        Returns:
            Manipuldate Instance
        """
        return self.add_month()

    def sub_month(self):
        """ Convenience method for subtracting one month.

        Returns:
            Manipuldate Instance
        """
        return self.sub_months(1)

    def last_month(self):
        """ Convenience method for subtracting one month.

        Returns:
            Manipuldate Instance
        """
        return self.sub_month()

    def add_week(self):
        """ Convenience method for adding one week.
        Returns:
            Manipuldate Instance
        """
        return self.add_weeks(1)

    def next_week(self):
        """ Convenience method for adding one week.

        Returns:
            Manipuldate Instance
        """
        return self.add_week()

    def sub_week(self):
        """ Convenience method for subtracting one week.

        Returns:
            Manipuldate Instance
        """
        return self.sub_weeks(1)

    def last_week(self):
        """ Convenience method for subtracting one week.

        Returns:
            Manipuldate Instance
        """
        return self.sub_week()

    def add_day(self):
        """ Convenience method for adding one day.

        Returns:
            Manipuldate Instance
        """
        return self.add_days(1)

    def tomorrow(self):
        """ Convenience method for adding one day.

        Returns:
            Manipuldate Instance
        """
        return self.add_day()

    def sub_day(self):
        """ Convenience method for subtracting one day.

        Returns:
            Manipuldate Instance
        """
        return self.sub_days(1)

    def yesterday(self):
        """ Convenience method for subtracting one day.

        Returns:
            Manipuldate Instance
        """
        return self.sub_day()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """                                                                                    """
    """                                   Date Logic                                       """
    """                                                                                    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def is_weekend(self):
        """ Returns a boolean answer to whether the current day is a weekend.

        Returns:
            Boolean
        """
        day_of_weeks = self.weekday()
        return day_of_weeks == self.SUNDAY or day_of_weeks == self.SATURDAY