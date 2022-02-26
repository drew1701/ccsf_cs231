#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 03: Task:
    Write a program that demonstrates a generator yielding progressively
    more accurate estimates of pi using the Liebniz formula
    pi = 4/1 - 4/3  + 4/5 - 4/7 + 4/9 - 4/11 ....
"""
# (b) uses generator expression, add CLA for max_repeat?, streamline?

max_repeat = 100
result = 0
sign = 1

# define generator expression
pi_expr = (4 * sign / denom for denom in range(1, max_repeat, 2))

# add running total to each iteration of generator, switch sign
for this in pi_expr:
    result += this
    print(result)
    sign *= -1
