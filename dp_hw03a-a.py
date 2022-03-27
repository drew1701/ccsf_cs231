#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 03: Task:
    Write a program that demonstrates a generator yielding progressively
    more accurate estimates of pi using the Liebniz formula
    pi = 4/1 - 4/3  + 4/5 - 4/7 + 4/9 - 4/11 ....
"""
# (a) uses generator function
# (a-a) uses exponent to switch sign
# (a-a) range starts 0, increments by 1, denominator updated


# creates generator function
def my_pi(max_repeats):
    result = 0
    for i in range(max_repeats):
        result += 4 * (-1)**i / (2 * i + 1)
        yield result


# use generator function to output iterations twords pi
for x in my_pi(100):
    print(x)
