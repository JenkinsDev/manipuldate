import unittest

from ..manipuldate import Manipuldate


class TestDateLogic(unittest.TestCase):

    def test_weekend_logic(self):
        # 11/22/2014 is a Saturday
        saturday_date = Manipuldate(2014, 11, 22)
        self.assertTrue(saturday_date.is_weekend())

        # 11/23/2014 is a Sunday
        sunday_date = Manipuldate(2014, 11, 23)
        self.assertTrue(sunday_date.is_weekend())

        # 11/24/2014 - 11/28/2014 are all weekdays (Monday - Friday)
        week_days = [24, 25, 26, 27, 28]
        for week_day in week_days:
            week_day_date = Manipuldate(2014, 11, week_day)
            self.assertFalse(week_day_date.is_weekend())

    def test_weekday_logic(self):
        # 11/22/2014 is a Saturday
        saturday_date = Manipuldate(2014, 11, 22)
        self.assertFalse(saturday_date.is_weekday())

        # 11/23/2014 is a Sunday
        sunday_date = Manipuldate(2014, 11, 23)
        self.assertFalse(sunday_date.is_weekday())

        # 11/24/2014 - 11/28/2014 are all weekdays (Monday - Friday)
        week_days = [24, 25, 26, 27, 28]
        for week_day in week_days:
            week_day_date = Manipuldate(2014, 11, week_day)
            self.assertTrue(week_day_date.is_weekday())


if __name__ == "__main__":
    unittest.main()