#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework XX: Task:
 Write a program that .
"""

print('this is testy2')

file = open('/users/abrick/resources/english', 'r').readlines()
print(len([line for line in file if line.strip() == line.strip()[::-1]]))

