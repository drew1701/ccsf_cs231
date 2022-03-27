#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 07: Task:
    Write a program that indicates how many times out of a thousand
    the Monte Carlo method is faster than the Liebniz formula at
    converging to within one thousandth of the true value of pi
"""
from math import pi
from random import uniform
from time import time


def find_pi_monte():
    this_pie = total_in = i = 0

    while abs(this_pie-pi) > pi/1000:
        x_point = uniform(-1, 1)
        y_point = uniform(-1, 1)
        if x_point**2 + y_point**2 < 1:
            total_in += 1

        i += 1
        this_pie = 4 * (total_in / i)

    return this_pie, i


def find_pi_lieb():
    this_pie = i = 0

    while abs(this_pie-pi) > pi/1000:
        this_pie += 4 * (-1)**i / (2 * i + 1)
        i += 1

    return this_pie, i


def main():
    race_count = 1000
    win_log = {
        "monte": 0,
        "lieb": 0,
    }

    for race in range(race_count):
        # Speed Test Monte Carlo
        start_monte = time()
        result = find_pi_monte()
        end_monte = time()

        # Speed Test Liebnitz
        start_lieb = time()
        result = find_pi_lieb()
        end_lieb = time()

        # Compare results, add win to log
        if end_monte - start_monte < end_lieb - start_lieb:
            win_log['monte'] += 1
        if end_lieb - start_lieb < end_monte - start_monte:
            win_log['lieb'] += 1

    # Output Results
    print('After ' + str(race_count) + ' rounds of speed tests:')
    print('The Monte Carlo method was faster ' + str(win_log['monte'])
          + ' times.')
    print('The Liebnitz Formula was faster ' + str(win_log['lieb'])
          + ' times.')
    print('Leaving '
          + str(race_count - win_log['monte'] - win_log['lieb'])
          + ' tied matches.')


if __name__ == '__main__':
    main()
