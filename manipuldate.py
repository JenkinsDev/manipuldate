import datetime


class Manipuldate(datetime.datetime):
    """ Easy date/datetime manipulation with Python3.x+ """

    def _new_instance(self, year=0, month=0, day=0, hour=0, minute=0,
                      second=0, microsecond=0, tzinfo=None):
        """ Creates a new instance of Manipuldate based on the supplied information,
        if something is set to 0, None or False then we will use the corresponding
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
        return self._new_instance(year=year, month=month)

    def sub_month(self):
        """ Convenience method for subtracting 1 month, shorter than using
        sub_months, anmd more pythonic.

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
        return self._new_instance(year=year, month=month)

    def add_month(self):
        """ Convenience method for adding 1 month, shorter than using
        add_months, and more pythonic.

        Returns:
            Manipuldate Instance
        """
        return self.add_months(months=1)
