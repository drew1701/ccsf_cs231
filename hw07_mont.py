"""
Use Monte Carlo to get to within a thousandth of pi
acceptable_range = (pi-pi/1000, pi+pi/1000)
"""
from math import pi
import random


def find_pi_monte():
    this_pie = total_in = i = 0

    while abs(this_pie-pi) > pi/1000:
        x_point = random.uniform(-1, 1)
        y_point = random.uniform(-1, 1)
        if x_point ** 2 + y_point ** 2 < 1:
            total_in += 1

        i += 1
        this_pie = 4 * (total_in / i)

    return this_pie, i


def main():
    import time
    monte_log = []
    for this in range(1000):
        start_time = time.time()
        result = find_pi_monte()
        end_time = time.time()
        monte_log.append(end_time - start_time)
    print('After using Monte Carlo to find pi in 1000 tests:')
    print('Fastest Time: ' + str(min(monte_log)))
    print('Slowest Time: ' + str(max(monte_log)))
    print('Average Time: ' + str(sum(monte_log)/len(monte_log)))


if __name__ == '__main__':
    main()
