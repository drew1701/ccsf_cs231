#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 03: Task:
    Write a program that demonstrates a generator yielding progressively
    more accurate estimates of pi using the Liebniz formula
    pi = 4/1 - 4/3  + 4/5 - 4/7 + 4/9 - 4/11 ....
"""
# (a) first rough/working copy, next use generator expression

# creates generator function
def my_pi(max_repeats):
    res = 0
    sign = 1
    N = 1
    for i in range(max_repeats):
        res += 4 * sign / N
        yield res
        sign *= -1
        N += 2


# use generator function to output iterations twords pi
for x in my_pi(100):
    print(x)