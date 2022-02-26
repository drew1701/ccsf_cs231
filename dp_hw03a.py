#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 03: Task:
    Write a program that demonstrates a generator yielding progressively
    more accurate estimates of pi using the Liebniz formula
    pi = 4/1 - 4/3  + 4/5 - 4/7 + 4/9 - 4/11 ....
"""
# (a) uses generator function, can it be generator expression?


# creates generator function
def my_pi(max_repeats):
    result = 0
    sign = 1
    for i in range(1, max_repeats, 2):
        result += 4 * sign / i
        yield result
        sign *= -1


# use generator function to output iterations twords pi
for x in my_pi(100):
    print(x)
