import unittest
import datetime

from manipuldate import Manipuldate


class TestBasicDateArithmetic(unittest.TestCase):

    def setUp(self):
        # Create our instance of Manipuldate based on a set
        # date so we can solidly check the arithmetic
        self.manip = Manipuldate(2006, 11, 21)

    def test_add_one_year(self):
        one_year = self.manip.add_year()
        self.assertEqual(one_year.year, 2007)

    def test_add_ten_years(self):
        ten_years = self.manip.add_years(10)
        self.assertEqual(ten_years.year, 2016)

    def test_sub_one_year(self):
        one_year = self.manip.sub_year()
        self.assertEqual(one_year.year, 2005)

    def test_sub_ten_years(self):
        ten_years = self.manip.sub_years(10)
        self.assertEqual(ten_years.year, 1996)

    def test_add_one_month(self):
        one_month = self.manip.add_month()
        self.assertEqual(one_month.month, 12)

    def test_add_two_months_and_year_wraps(self):
        two_months = self.manip.add_months(2)
        self.assertEqual(two_months.month, 1)
        self.assertEqual(two_months.year, 2007)

    def test_add_one_hundred_months_and_year_wraps(self):
        # We want to make sure that when adding (n) months that the
        # year will always continuing wrapping until we have reached
        # the correct date.
        one_hundred_months = self.manip.add_months(100)
        self.assertEqual(one_hundred_months.month, 3)
        self.assertEqual(one_hundred_months.year, 2015)

    def test_sub_on_month(self):
        one_month = self.manip.sub_month()
        self.assertEqual(one_month.month, 10)

    def test_sub_eleven_months_and_year_wraps(self):
        eleven_months = self.manip.sub_months(11)
        self.assertEqual(eleven_months.month, 12)
        self.assertEqual(eleven_months.year, 2005)

    def test_sub_one_hundred_months_and_year_wraps(self):
        one_hundred_months = self.manip.sub_months(100)
        self.assertEqual(one_hundred_months.month, 7)
        self.assertEqual(one_hundred_months.year, 1998)

    def test_we_can_do_multiple_equations_chained(self):
        new_date = self.manip.add_year().sub_months(10)
        self.assertEqual(new_date.year, 2007)
        self.assertEqual(new_date.month, 1)

        # Let's try with some more arithmetic.
        newer_date = self.manip.add_months(24).sub_years(2)
        self.assertEqual(newer_date.year, 2006)
        self.assertEqual(newer_date.month, 11)

    def test_addition_of_weeks(self):
        one_week = self.manip.add_week()
        two_weeks = self.manip.add_weeks(2)
        self.assertEqual(one_week.day, 28)
        self.assertEqual(two_weeks.month, 12)
        self.assertEqual(two_weeks.day, 5)

    def test_addition_of_days_works(self):
        one_day = self.manip.add_day()
        three_days = self.manip.add_days(3)
        self.assertEqual(one_day.day, 22)
        self.assertEqual(three_days.day, 24)

    def test_subtraction_of_days(self):
        one_day = self.manip.sub_day()
        three_days = self.manip.sub_days(3)
        self.assertEqual(one_day.day, 20)
        self.assertEqual(three_days.day, 18)



class TestManipuldateInstances(unittest.TestCase):

    def setUp(self):
        self.d = datetime.date.today()
        self.t = datetime.time(10, 30, 41, 1)
        self.dt = datetime.datetime.now()
        self.manip = Manipuldate.strptime("11/21/06", "%m/%d/%y")

    def test_creating_instance_from_datetime_returns_manipuldate(self):
        manip = Manipuldate.from_datetime(self.dt)
        self.assertTrue(isinstance(manip, Manipuldate))

    def test_creating_instance_from_date_returns_manipuldate(self):
        manip = Manipuldate.from_date(self.d)
        self.assertTrue(isinstance(manip, Manipuldate))

    def test_crreating_instance_from_time_returns_manipuldate(self):
        manip = Manipuldate.from_time(self.t)
        self.assertTrue(isinstance(manip, Manipuldate))

    def test_response_is_instance_of_manipuldate_on_addition(self):
        one_month = self.manip.add_month()
        one_year = self.manip.add_year()
        one_day = self.manip.add_day()
        self.assertTrue(isinstance(one_month, Manipuldate))
        self.assertTrue(isinstance(one_year, Manipuldate))
        self.assertTrue(isinstance(one_day, Manipuldate))

    def test_response_is_instance_of_manipuldate_on_subtraction(self):
        one_month = self.manip.sub_month()
        one_year = self.manip.sub_year()
        self.assertTrue(isinstance(one_month, Manipuldate))
        self.assertTrue(isinstance(one_year, Manipuldate))


class TestManipuldateInstanceCopyingPreservesData(unittest.TestCase):

    def setUp(self):
        self.d = datetime.date.today()
        self.t = datetime.time(10, 30, 41, 1)
        self.dt = datetime.datetime.now()

    def test_creating_instance_from_datetime_preserves_data(self):
        manip = Manipuldate.from_datetime(self.dt)
        # Now we check each and every attribute.
        self.assertEqual(manip.year, self.dt.year)
        self.assertEqual(manip.month, self.dt.month)
        self.assertEqual(manip.day, self.dt.day)
        self.assertEqual(manip.hour, self.dt.hour)
        self.assertEqual(manip.minute, self.dt.minute)
        self.assertEqual(manip.second, self.dt.second)
        self.assertEqual(manip.microsecond, self.dt.microsecond)
        self.assertEqual(manip.tzinfo, self.dt.tzinfo)

    def test_creating_instance_from_date_preserves_data(self):
        manip = Manipuldate.from_date(self.d)
        # Now we check all of the date attributes.
        self.assertEqual(manip.year, self.d.year)
        self.assertEqual(manip.month, self.d.month)
        self.assertEqual(manip.day, self.d.day)

    def test_creating_instance_from_time_preserves_data(self):
        manip = Manipuldate.from_time(self.t)
        # Now we check all of the time attributes.
        self.assertEqual(manip.hour, self.t.hour)
        self.assertEqual(manip.minute, self.t.minute)
        self.assertEqual(manip.second, self.t.second)
        self.assertEqual(manip.microsecond, self.t.microsecond)
        self.assertEqual(manip.tzinfo, self.t.tzinfo)
        # Just because with datetime the year, month and day are required
        # we will go ahead and check to make sure they are set to 1/1/1970
        self.assertEqual(manip.year, 1970)
        self.assertEqual(manip.month, 1)
        self.assertEqual(manip.day, 1)


if __name__ == "__main__":
    unittest.main()