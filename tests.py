import unittest

from manipuldate import Manipuldate


class TestBasicDateArithmetic(unittest.TestCase):

    def setUp(self):
        # Create our instance of Manipuldate based on a set
        # date so we can solidly check the arithmetic
        self.manip = Manipuldate.strptime("11/21/06", "%m/%d/%y")

    def test_response_is_instance_of_manipuldate_addition(self):
        one_month = self.manip.add_month()
        self.assertTrue(isinstance(one_month, Manipuldate))

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


if __name__ == "__main__":
    unittest.main()