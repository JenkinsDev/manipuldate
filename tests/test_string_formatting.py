import unittest

from manipuldate import Manipuldate
from datetime import datetime, date


class TestStringFormatting(unittest.TestCase):

    def setUp(self):
        self.manip = Manipuldate(year=2005, month=5, day=15)
        self.manip_date = Manipuldate.from_date(date(year=2005, month=5, day=15))
        self.manip_dt = Manipuldate(year=2005, month=5, day=15, hour=10, minute=50, second=20)
        self.today = Manipuldate.today()

    def test_default_string_formatting_is_in_place(self):
        self.assertEqual(str(self.manip), "2005-05-15 00:00:00")

    def test_instance_creation_methods_add_default_string_format(self):
        default_format = Manipuldate.DEFAULT_STRING_FORMAT
        today_str = str(self.today)
        datetime_today_str = str(datetime.today().strftime(default_format))
        self.assertEqual(today_str, datetime_today_str)
        self.assertEqual(str(self.manip_date), "2005-05-15 00:00:00")

    def test_full_datetime_is_formatting(self):
        self.assertEqual(str(self.manip_dt), "2005-05-15 10:50:20")

    def test_overriding_string_formatting(self):
        manip = self.manip_dt
        manip.set_string_format("%Y/%m/%d %H-%M-%S")
        self.assertEqual(str(manip), "2005/05/15 10-50-20")

if __name__ == "__main__":
    unittest.main()
