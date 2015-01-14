import datetime

from .enums import DaysOfWeek, DateTimeDefaults


class Manipuldate(datetime.datetime):
    """ Easy date/time/datetime manipulation with Python3.x+ """

    DEFAULT_STRING_FORMAT = 'Y-m-d H:i:s'

    ############################################################################
    ###                                                                      ###
    ###                      Initialization Methods                          ###
    ###                                                                      ###
    ############################################################################

    @classmethod
    def tomorrow(cls):
        """ Convenience method that will create a Manipuldate for tomorrow.

        Returns:
            Manipuldate Instance
        """
        return cls.today().add_day()

    @classmethod
    def yesterday(cls):
        """ Convenience method that will create a Manipuldate for yesterday.

        Returns:
            Manipuldate Instance
        """
        return cls.today().sub_day()

    @classmethod
    def next_week(cls):
        """ Convenience method that will create a Manipuldate for next week.
        This method will just add seven days to today.

        Returns:
            Manipuldate Instance
        """
        return cls.today().add_week()

    @classmethod
    def last_week(cls):
        """ Convenience method that will create a Manipuldate for next week.
        This method will just subtract seven days to today.

        Returns:
            Manipuldate Instance
        """
        return cls.today().sub_week()

    @classmethod
    def next_month(cls):
        """ Convenience method that will create a Manipuldate for next week.
        This method will add 1 to the current (today's) month.

        Returns:
            Manipuldate Instance
        """
        return cls.today().add_month()

    @classmethod
    def last_month(cls):
        """ Convenience method that will create a Manipuldate for next week.
        This method will subtract 1 to the current (today's) month.

        Returns:
            Manipuldate Instance
        """
        return cls.today().sub_month()

    @classmethod
    def next_year(cls):
        """ Convenience method that will create a Manipuldate for next week.
        This method will add 1 to the current (today's) year.

        Returns:
            Manipuldate Instance
        """
        return cls.today().add_year()

    @classmethod
    def last_year(cls):
        """ Convenience method that will create a Manipuldate for next week.
        This method will subtract 1 to the current (today's) year.

        Returns:
            Manipuldate Instance
        """
        return cls.today().sub_year()

    @classmethod
    def from_datetime(cls, dt):
        """ Creates an instance of Manipuldate based on a supplied datetime
        instance.

        Parameters:
            :param dt: Datetime instance that we will be using to create our
                       instance.

        Returns:
            Manipuldate Instance
        """
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute,
                           dt.second, dt.microsecond, dt.tzinfo)

    @classmethod
    def from_date(cls, d):
        """ Creates an instance of Manipuldate based on a supplied date instance.

        Parameters:
            :param d: Date instance that we will be using to create our new
                      instance.

        Returns:
            Manipuldate Instance
        """
        return cls(d.year, d.month, d.day)

    @classmethod
    def from_time(cls, t):
        """ Creates an instance of Manipuldate based on the supplied time
        instance.

        Parameters:
            :param t: Time instance that we will be using to create our new
                      instance.

        Returns:
            Manipuldate Instance
        """
        # Year, month and day are required by the datetime class which we
        # extend with manipuldate.
        return cls(1970, 1, 1, t.hour, t.minute, t.second,
                           t.microsecond, t.tzinfo)

    def _copy_to_new_instance(self, year=None, month=None, day=None, hour=None,
                              minute=None, second=None, microsecond=None,
                              tzinfo=None):
        """ Creates a new instance of Manipuldate based on the supplied
        information, if something is set to None or False then we will use the
        corresponding attributes value.

        Parameters:
            :param year: Numerical value that represents years
            :param month: Numerical value that represents months [1-12]
            :param day: Numerical value that represents days [1-(28-31)]
            :param hour: Numerical value that represents hours [0-24]
            :param minute: Numerical value that represents minutes [0-60]
            :param second: Numerical value that represents seconds [0-60]
            :param second: Numerical value that represents microseconds
                           [0-1000000]
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
        return Manipuldate(year, month, day, hour, minute, second, microsecond,
                           tzinfo)

    ############################################################################
    ###                                                                      ###
    ###                          Date Arithmetic                             ###
    ###                                                                      ###
    ############################################################################

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
        return self.add_days(DateTimeDefaults.DAYS_IN_WEEK.value * weeks)

    def sub_weeks(self, weeks):
        """ Subtracts n-weeks * 7 days form the current date.

        Parameters:
            :param weeks: N-weeks to subtract from the current date.
        """
        return self.sub_days(DateTimeDefaults.DAYS_IN_WEEK.value * weeks)

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

    ################### DATE ARITHMETIC CONVENIENCE METHODS ####################

    def add_year(self):
        """ Convenience method for adding one year.

        Returns:
            Manipuldate Instance
        """
        return self.add_years(1)

    def sub_year(self):
        """ Convenience method for subtracting one year.

        Returns:
            Manipuldate Instance
        """
        return self.sub_years(1)

    def add_month(self):
        """ Convenience method for adding one month.

        Returns:
            Manipuldate Instance
        """
        return self.add_months(months=1)

    def sub_month(self):
        """ Convenience method for subtracting one month.

        Returns:
            Manipuldate Instance
        """
        return self.sub_months(1)

    def add_week(self):
        """ Convenience method for adding one week.
        Returns:
            Manipuldate Instance
        """
        return self.add_weeks(1)

    def sub_week(self):
        """ Convenience method for subtracting one week.

        Returns:
            Manipuldate Instance
        """
        return self.sub_weeks(1)

    def add_day(self):
        """ Convenience method for adding one day.

        Returns:
            Manipuldate Instance
        """
        return self.add_days(1)

    def sub_day(self):
        """ Convenience method for subtracting one day.

        Returns:
            Manipuldate Instance
        """
        return self.sub_days(1)

    ############################################################################
    ###                                                                      ###
    ###                            Date Logic                                ###
    ###                                                                      ###
    ############################################################################

    def is_weekend(self):
        """ Returns a boolean answer that answers whether or not the current
        date is a weekend.

        Returns:
            Boolean
        """
        day_of_weeks = self.weekday()
        return day_of_weeks == DaysOfWeek.Sunday.value or \
               day_of_weeks == DaysOfWeek.Saturday.value

    def is_weekday(self):
        """ Returns a boolean answer that answers whether or not the current
        date is a weekday.

        Returns:
            Boolean
        """
        return not self.is_weekend()
