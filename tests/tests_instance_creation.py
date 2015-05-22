import unittest
import datetime

from manipuldate import Manipuldate


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

    def test_creating_instance_from_time_returns_manipuldate(self):
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

    def test_creating_instance_for_max_date_is_correct(self):
        max_month = 12
        max_day = 31
        max_year = datetime.MAXYEAR
        max_date = datetime.datetime(year=max_year, month=max_month, day=max_day)
        self.assertEqual(str(Manipuldate.max_date()), str(max_date))

    def test_creating_instance_for_min_date_is_correct(self):
        min_month = 1
        min_day = 1
        min_year = datetime.MINYEAR
        min_date = datetime.datetime(year=min_year, month=min_month, day=min_day)
        self.assertEqual(str(Manipuldate.min_date()), str(min_date))


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
        # we will go ahead and check to make sure they are set to 1/1/0001
        self.assertEqual(manip.year, 1)
        self.assertEqual(manip.month, 1)
        self.assertEqual(manip.day, 1)


if __name__ == "__main__":
    unittest.main()
