"""
Homework 03
    Write a program that demonstrates a generator yielding progressively
    more accurate estimates of pi using the Liebniz formula
"""

max_repeat = 100
result = 0
sign = 1

# setup generator expression
pi_expr = (4 * sign / denom for denom in range(1, max_repeat, 2))

# add running total to each iteration of generator, switch sign
for each in pi_expr:
    result += each
    print(result)
    sign *= -1
