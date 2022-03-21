#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 06: Task:
    Use unittest.TestCase methods to confirm that the addition and
    subtraction of date and timedelta objects produce correct results
"""
import unittest
import datetime


class MyTimedeltaTest(unittest.TestCase):
    """
    Test adding/subtracting from date objects with timedelta
    """

    def test_add_days(self):
        # start and end day values set manually
        start_day = datetime.date(2022, 2, 2)
        end_day = datetime.date(2022, 2, 5)
        # result value derived for test comparison
        result = start_day + datetime.timedelta(days=3)
        self.assertEqual(result, end_day)

    def test_subtract_days(self):
        start_day = datetime.date(2022, 2, 2)
        end_day = datetime.date(2022, 1, 30)
        result = start_day + datetime.timedelta(days=-3)
        self.assertEqual(result, end_day)

    def test_add_weeks(self):
        start_day = datetime.date(2022, 2, 2)
        end_day = datetime.date(2022, 2, 16)
        result = start_day + datetime.timedelta(weeks=2)
        self.assertEqual(result, end_day)

    def test_subtract_weeks(self):
        start_day = datetime.date(2022, 2, 2)
        end_day = datetime.date(2022, 1, 19)
        result = start_day + datetime.timedelta(weeks=-2)
        self.assertEqual(result, end_day)


if __name__ == '__main__':
    # unittest verbose output enabled
    unittest.main(verbosity=2)
