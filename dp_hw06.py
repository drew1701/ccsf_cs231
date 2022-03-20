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
    Test the add/subtract functions from timedelta
    """

    def test_add_days(self):
        start_day = datetime.date(2022, 2, 2)
        end_day = datetime.date(2022, 2, 5)
        result = start_day + datetime.timedelta(days=3)
        self.assertEqual(result, end_day)

    def test_subtract_days(self):
        start_day = datetime.date(2022, 2, 2)
        end_day = datetime.date(2022, 1, 30)
        result = start_day + datetime.timedelta(days=-3)
        self.assertEqual(result, end_day)


if __name__ == '__main__':
    unittest.main()
