import unittest

from manipuldate import Manipuldate


class TestBasicDateArithmetic(unittest.TestCase):

    def setUp(self):
        # Create our instance of Manipuldate based on a set
        # date so we can solidly check the arithmetic
        self.manip = Manipuldate(2006, 11, 21)

    def test_add_ten_years(self):
        ten_years = self.manip.add_years(10)
        self.assertEqual(ten_years.year, 2016)

    def test_sub_ten_years(self):
        ten_years = self.manip.sub_years(10)
        self.assertEqual(ten_years.year, 1996)

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
        two_weeks = self.manip.add_weeks(2)
        self.assertEqual(two_weeks.month, 12)
        self.assertEqual(two_weeks.day, 5)

    def test_subtraction_of_weeks(self):
        sub_two_weeks = self.manip.sub_weeks(2)
        self.assertEqual(sub_two_weeks.month, 11)
        self.assertEqual(sub_two_weeks.day, 7)

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


class TestDateArithmeticConvenienceMethods(unittest.TestCase):

    def setUp(self):
        self.manip = Manipuldate(2006, 11, 21)

    def test_addition_year_convenience_methods(self):
        add_one_year = self.manip.add_year()
        next_year = self.manip.next_year()
        self.assertEqual(add_one_year.year, 2007)
        self.assertEqual(add_one_year, next_year)

    def test_subtraction_year_convenience_methods(self):
        sub_one_year = self.manip.sub_year()
        last_year = self.manip.last_year()
        self.assertEqual(sub_one_year.year, 2005)
        self.assertEqual(sub_one_year, last_year)

    def test_addition_month_convenience_methods(self):
        add_one_month = self.manip.add_month()
        next_month = self.manip.next_month()
        self.assertEqual(add_one_month.month, 12)
        self.assertEqual(add_one_month, next_month)

    def test_subtraction_month_convenience_methods(self):
        sub_one_month = self.manip.sub_month()
        last_month = self.manip.last_month()
        self.assertEqual(sub_one_month.month, 10)
        self.assertEqual(sub_one_month, last_month)

    def test_addition_week_convenience_methods(self):
        add_one_week = self.manip.add_week()
        next_week = self.manip.next_week()
        self.assertEqual(add_one_week.day, 28)
        self.assertEqual(add_one_week, next_week)

    def test_subtraction_week_convenience_methods(self):
        sub_one_week = self.manip.sub_week()
        last_week = self.manip.last_week()
        self.assertEqual(sub_one_week.day, 14)
        self.assertEqual(sub_one_week, last_week)

    def test_addition_day_convenience_methods(self):
        add_one_day = self.manip.add_day()
        tomorrow = self.manip.tomorrow()
        self.assertEqual(add_one_day.day, 22)
        self.assertEqual(add_one_day, tomorrow)

    def test_subtraction_day_convenience_methods(self):
        sub_one_day = self.manip.sub_day()
        yesterday = self.manip.yesterday()
        self.assertEqual(sub_one_day.day, 20)
        self.assertEqual(sub_one_day, yesterday)


if __name__ == "__main__":
    unittest.main()
