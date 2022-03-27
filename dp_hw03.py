#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 03: Task:
    Write a program that demonstrates a generator yielding progressively
    more accurate estimates of pi using the Liebniz formula
    pi = 4/1 - 4/3  + 4/5 - 4/7 + 4/9 - 4/11 ....
"""
max_repeat = 100
result = 0

# define generator expression
pi_expr = (4 * (-1)**i / (2 * i + 1) for i in range(max_repeat))

# add running total to each iteration of generator
for this in pi_expr:
    result += this
    print(result)
