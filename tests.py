import unittest
import datetime

from manipuldate import Manipuldate


class TestBasicDateArithmetic(unittest.TestCase):

    def setUp(self):
        # Create our instance of Manipuldate based on a set
        # date so we can solidly check the arithmetic
        self.manip = Manipuldate.strptime("11/21/06", "%m/%d/%y")

    def test_add_one_month(self):
        one_month = self.manip.add_month()
        self.assertEqual(one_month.month, 12)

    def test_add_two_months_and_year_wraps(self):
        two_months = self.manip.add_months(2)
        self.assertEqual(two_months.month, 1)
        self.assertEqual(two_months.year, 2007)

    def test_add_one_hundred_months_and_year_wrap(self):
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


class TestManipuldateInstances(unittest.TestCase):

    def setUp(self):
        self.d = datetime.date.today()
        self.dt = datetime.datetime.now()
        self.manip = Manipuldate.strptime("11/21/06", "%m/%d/%y")

    def test_creating_instance_from_datetime_returns_manipuldate(self):
        manip = Manipuldate.instance(self.dt)
        self.assertTrue(isinstance(manip, Manipuldate))

    def test_creating_instance_from_date_returns_manipuldate(self):
        manip = Manipuldate.instance_from_date(self.d)
        self.assertTrue(isinstance(manip, Manipuldate))

    def test_response_is_instance_of_manipuldate_on_addition(self):
        one_month = self.manip.add_month()
        self.assertTrue(isinstance(one_month, Manipuldate))

    def test_response_is_instance_of_manipuldate_on_subtraction(self):
        one_month = self.manip.sub_month()
        self.assertTrue(isinstance(one_month, Manipuldate))


class TestManipuldateInstanceCopyingPreservesData(unittest.TestCase):

    def setUp(self):
        self.d = datetime.date.today()
        self.dt = datetime.datetime.now()

    def test_creating_instance_from_datetime_preserves_data(self):
        manip = Manipuldate.instance(self.dt)
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
        manip = Manipuldate.instance_from_date(self.d)
        # Now we check all of the date attributes.
        self.assertEqual(manip.year, self.d.year)
        self.assertEqual(manip.month, self.d.month)
        self.assertEqual(manip.day, self.d.day)


if __name__ == "__main__":
    unittest.main()