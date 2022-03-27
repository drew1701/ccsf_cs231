"""
Use liebnitz to get to within a thousandth of pi
acceptable_range = (pi-pi/1000, pi+pi/1000)
"""
from math import pi


def find_pi_lieb():
    this_pie = i = 0

    while abs(this_pie-pi) > pi/1000:
        this_pie += 4 * (-1)**i / (2 * i + 1)
        i += 1

    return this_pie, i


def main():
    import time
    lieb_log = []
    for this in range(1000):
        start_time = time.time()
        result = find_pi_lieb()
        end_time = time.time()
        lieb_log.append(end_time - start_time)
    print('After using Liebnitz to find pi in 1000 tests:')
    print('Fastest Time: ' + str(min(lieb_log)))
    print('Slowest Time: ' + str(max(lieb_log)))
    print('Average Time: ' + str(sum(lieb_log)/len(lieb_log)))


if __name__ == '__main__':
    main()
