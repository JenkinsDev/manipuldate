import unittest

from manipuldate import Manipuldate


class TestDateLogic(unittest.TestCase):

    def setUp(self):
        # 11/17/2014 is a Monday
        self.monday_date = Manipuldate(2014, 11, 17)
        # 11/18/2014 is a Tuesday
        self.tuesday_date = Manipuldate(2014, 11, 18)
        # 11/19/2014 is a Wednesday
        self.wednesday_date = Manipuldate(2014, 11, 19)
        # 11/20/2014 is a Thursday
        self.thursday_date = Manipuldate(2014, 11, 20)
        # 11/21/2014 is a Friday
        self.friday_date = Manipuldate(2014, 11, 21)
        # 11/22/2014 is a Saturday
        self.saturday_date = Manipuldate(2014, 11, 22)
        # 11/23/2014 is a Sunday
        self.sunday_date = Manipuldate(2014, 11, 23)

    def test_weekend_logic(self):
        self.assertTrue(self.saturday_date.is_weekend())
        self.assertTrue(self.sunday_date.is_weekend())

        # 11/24/2014 - 11/28/2014 are all weekdays (Monday - Friday)
        week_days = [24, 25, 26, 27, 28]
        for week_day in week_days:
            week_day_date = Manipuldate(2014, 11, week_day)
            self.assertFalse(week_day_date.is_weekend())

    def test_weekday_logic(self):
        self.assertFalse(self.saturday_date.is_weekday())
        self.assertFalse(self.sunday_date.is_weekday())

        # 11/24/2014 - 11/28/2014 are all weekdays (Monday - Friday)
        week_days = [24, 25, 26, 27, 28]
        for week_day in week_days:
            week_day_date = Manipuldate(2014, 11, week_day)
            self.assertTrue(week_day_date.is_weekday())

    def test_is_monday_logic(self):
        self.assertTrue(self.monday_date.is_monday())
        self.assertFalse(self.tuesday_date.is_monday())
        self.assertFalse(self.wednesday_date.is_monday())
        self.assertFalse(self.thursday_date.is_monday())
        self.assertFalse(self.friday_date.is_monday())
        self.assertFalse(self.saturday_date.is_monday())
        self.assertFalse(self.sunday_date.is_monday())

    def test_is_tuesday_logic(self):
        self.assertFalse(self.monday_date.is_tuesday())
        self.assertTrue(self.tuesday_date.is_tuesday())
        self.assertFalse(self.wednesday_date.is_tuesday())
        self.assertFalse(self.thursday_date.is_tuesday())
        self.assertFalse(self.friday_date.is_tuesday())
        self.assertFalse(self.saturday_date.is_tuesday())
        self.assertFalse(self.sunday_date.is_tuesday())

    def test_is_wednesday_logic(self):
        self.assertFalse(self.monday_date.is_wednesday())
        self.assertFalse(self.tuesday_date.is_wednesday())
        self.assertTrue(self.wednesday_date.is_wednesday())
        self.assertFalse(self.thursday_date.is_wednesday())
        self.assertFalse(self.friday_date.is_wednesday())
        self.assertFalse(self.saturday_date.is_wednesday())
        self.assertFalse(self.sunday_date.is_wednesday())

    def test_is_thursday_logic(self):
        self.assertFalse(self.monday_date.is_thursday())
        self.assertFalse(self.tuesday_date.is_thursday())
        self.assertFalse(self.wednesday_date.is_thursday())
        self.assertTrue(self.thursday_date.is_thursday())
        self.assertFalse(self.friday_date.is_thursday())
        self.assertFalse(self.saturday_date.is_thursday())
        self.assertFalse(self.sunday_date.is_thursday())

    def test_is_friday_logic(self):
        self.assertFalse(self.monday_date.is_friday())
        self.assertFalse(self.tuesday_date.is_friday())
        self.assertFalse(self.wednesday_date.is_friday())
        self.assertFalse(self.thursday_date.is_friday())
        self.assertTrue(self.friday_date.is_friday())
        self.assertFalse(self.saturday_date.is_friday())
        self.assertFalse(self.sunday_date.is_friday())

    def test_is_saturday_logic(self):
        self.assertFalse(self.monday_date.is_saturday())
        self.assertFalse(self.tuesday_date.is_saturday())
        self.assertFalse(self.wednesday_date.is_saturday())
        self.assertFalse(self.thursday_date.is_saturday())
        self.assertFalse(self.friday_date.is_saturday())
        self.assertTrue(self.saturday_date.is_saturday())
        self.assertFalse(self.sunday_date.is_saturday())

    def test_is_sunday_logic(self):
        self.assertFalse(self.monday_date.is_sunday())
        self.assertFalse(self.tuesday_date.is_sunday())
        self.assertFalse(self.wednesday_date.is_sunday())
        self.assertFalse(self.thursday_date.is_sunday())
        self.assertFalse(self.friday_date.is_sunday())
        self.assertFalse(self.saturday_date.is_sunday())
        self.assertTrue(self.sunday_date.is_sunday())


if __name__ == "__main__":
    unittest.main()
