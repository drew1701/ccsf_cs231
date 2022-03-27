#!/usr/bin/env python3
"""
Homework 07
    Write a program that indicates how many times out of a thousand
    the Monte Carlo method is faster than the Liebniz formula at
    converging to within one thousandth of the true value of pi
"""
from math import pi
from random import uniform
from time import time


def find_pi_monte():
    # Set tracking variables to zero, i for increment.
    this_pie = total_in = i = 0

    # Loop until estimated pi is within acceptable range.
    while abs(this_pie-pi) > pi/1000:
        x_point = uniform(-1, 1)
        y_point = uniform(-1, 1)
        # If x,y point is within unit circle, increment total_in.
        if x_point**2 + y_point**2 < 1:
            total_in += 1
        # Increment counter, estimate pi using Monte Carlo method.
        i += 1
        this_pie = 4 * (total_in / i)

    # Return matching pi estimate and number of iterations.
    return this_pie, i


def find_pi_lieb():
    # Set tracking variables to zero, i for increment.
    this_pie = i = 0

    # Loop until estimated pi is within acceptable range.
    while abs(this_pie-pi) > pi/1000:
        # Estimate pi using Liebnitz formula, increment counter.
        this_pie += 4 * (-1)**i / (2 * i + 1)
        i += 1

    # Return matching pi estimate and number of iterations.
    return this_pie, i


def main():
    # Set race_count and define dict to track wins.
    race_count = 1000
    win_log = {
        "monte": 0,
        "lieb": 0,
    }

    # Perform race_count number of speed races.
    for race in range(race_count):
        # Speed Test using Monte Carlo method.
        start_monte = time()
        result = find_pi_monte()
        end_monte = time()
        # Speed Test using Liebnitz formula.
        start_lieb = time()
        result = find_pi_lieb()
        end_lieb = time()

        # Compare results, add winner to win_log.
        if end_monte - start_monte < end_lieb - start_lieb:
            win_log['monte'] += 1
        if end_lieb - start_lieb < end_monte - start_monte:
            win_log['lieb'] += 1

    # Output results including race count, wins, and ties.
    print('After ' + str(race_count) + ' rounds of speed tests:')
    print('The Monte Carlo method was faster '
          + str(win_log['monte']) + ' times.')
    print('The Liebnitz formula was faster '
          + str(win_log['lieb']) + ' times.')
    print('Leaving '
          + str(race_count - win_log['monte'] - win_log['lieb'])
          + ' tied matches.')


if __name__ == '__main__':
    main()
