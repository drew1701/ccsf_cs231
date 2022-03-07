#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework XX: Task:
 Write a program that .
"""
from datetime import datetime

date_str = '14/Aug/2017:09:42:29 -0700'
format_code = '%d/%b/%Y:%H:%M:%S -0700'

dt_object = datetime.strptime(date_str, format_code)

print(dt_object)


