import datetime

from .enums import DaysOfWeek, DateTimeDefaults


class Manipuldate(datetime.datetime):
    """ Easy date/time/datetime manipulation with Python3.x+ """

    DEFAULT_STRING_FORMAT = 'Y-m-d H:i:s'

    MIN_YEAR = 1970
    MIN_MONTH = 1
    MIN_DAY = 1

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
        return cls(cls.MIN_YEAR, cls.MIN_MONTH, cls.MIN_DAY, t.hour, t.minute,
                           t.second, t.microsecond, t.tzinfo)

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
        return self.replace(year=self.year + years)

    def sub_years(self, years):
        """ Subtracts the amount of provided years from our datetime object
        then returns a new instance of Manipuldate because of how datetime
        works within python, no editable properties.

        Parameters:
            :param years: The number of years to sub from the current date.

        Returns:
            Manipuldate Instance
        """
        return self.replace(year=self.year - years)

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
        return self.replace(year=year, month=month)

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
        return self.replace(year=year, month=month)

    def add_weeks(self, weeks):
        """ Adds n-weeks * 7 days to the current date.

        Parameters:
            :param weeks: N weeks to add to the current date.

        Returns:
            Manipuldate Instance
        """
        return self.add_days(DateTimeDefaults.Days_In_Week.value * weeks)

    def sub_weeks(self, weeks):
        """ Subtracts n-weeks * 7 days form the current date.

        Parameters:
            :param weeks: N-weeks to subtract from the current date.
        """
        return self.sub_days(DateTimeDefaults.Days_In_Week.value * weeks)

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
        """ Checks to see if the instance's date falls on a weekend.

        Returns:
            Boolean
        """
        day_of_week = self.weekday()
        return day_of_week == DaysOfWeek.Sunday.value or \
               day_of_week == DaysOfWeek.Saturday.value

    def is_weekday(self):
        """ Checks to see if the instance's date falls on a weekday.

        Returns:
            Boolean
        """
        return not self.is_weekend()

    def is_monday(self):
        """ Checks to see if the instance's date falls on a Monday.

        Returns:
            Boolean
        """
        return self.weekday() == DaysOfWeek.Monday.value

    def is_tuesday(self):
        """ Checks to see if the instance's date falls on a Tuesday.

        Returns:
            Boolean
        """
        return self.weekday() == DaysOfWeek.Tuesday.value

    def is_wednesday(self):
        """ Checks to see if the instance's date falls on a Wednesday.

        Returns:
            Boolean
        """
        return self.weekday() == DaysOfWeek.Wednesday.value

    def is_thursday(self):
        """ Checks to see if the instance's date falls on a Thursday.

        Returns:
            Boolean
        """
        return self.weekday() == DaysOfWeek.Thursday.value

    def is_friday(self):
        """ Checks to see if the instance's date falls on a Friday.

        Returns:
            Boolean
        """
        return self.weekday() == DaysOfWeek.Friday.value

    def is_saturday(self):
        """ Checks to see if the instance's date falls on a Saturday.

        Returns:
            Boolean
        """
        return self.weekday() == DaysOfWeek.Saturday.value

    def is_sunday(self):
        """ Checks to see if the instance's date falls on a Sunday.

        Returns:
            Boolean
        """
        return self.weekday() == DaysOfWeek.Sunday.value
