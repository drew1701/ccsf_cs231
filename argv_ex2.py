#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 08: Task:
    sys.argv example 2
"""
import sys

print(f"Arguments count: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
    print(f"Argument {i:>6}: {arg}")
