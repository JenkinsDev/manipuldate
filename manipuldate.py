import datetime


class Manipuldate(datetime.datetime):
    """ Easy date/datetime manipulation with Python3.x+ """

    def _new_instance(self, year=0, month=0, day=0, hour=0, minute=0,
                      second=0, microsecond=0, tzinfo=None):
        year = year or self.year
        month = month or self.month
        day = day or self.day
        hour = hour or self.hour
        minute = minute or self.minute
        second = second or self.second
        microsecond = microsecond or self.microsecond
        tzinfo = tzinfo or self.tzinfo
        return Manipuldate(year, month, day, hour, minute, second, microsecond, tzinfo)

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
        """ Convenience method for add 1 month, shorter than
        using add_months, and more pythonic.

        Returns:
            Manipuldate Instance
        """
        return self.add_months(months=1)
