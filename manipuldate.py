import datetime


class Manipuldate(datetime.datetime):
    """ Easy date/time/datetime manipulation with Python3.x+ """

    SECONDS_IN_DAY = 60 * 60 * 24
    DEFAULT_TO_STRING_FORMAT = 'Y-m-d H:i:s'

    @staticmethod
    def instance(dt):
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

    def sub_months(self, months):
        """ Subtracts the amount of provided months to our datetime object
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

    def sub_month(self):
        """ Convenience method for subtracting 1 month, shorter than using
        sub_months, and more pythonic.

        Returns:
            Manipuldate Instance
        """
        return self.sub_months(1)

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

    def add_month(self):
        """ Convenience method for adding 1 month, shorter than using
        add_months, and more pythonic.

        Returns:
            Manipuldate Instance
        """
        return self.add_months(months=1)
