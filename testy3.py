#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework XX: Task:
 Write a program that .
"""

'''
from datetime import datetime

date_str = '14/Aug/2017:09:42:29 -0700'
format_code = '%d/%b/%Y:%H:%M:%S -0700'

dt_object = datetime.strptime(date_str, format_code)

print(dt_object)
'''

from datetime import datetime
import sys


def time_read(access_log):

    for Access in open('/etc/httpd/logs/access_log', "r"):
        yield Access

time_gen = time_read("/etc/httpd/logs/access_log")

Access_count = 0

for row in time_gen:
    Access_count += 1

print()
print("Log '/etc/httpd/logs/access_log' was created in 14 August 2017.")
print(f"The number of accesses made in each hour from the beginning '(since it was created)' of '/etc/httpd/logs/access_log' up until 11pm on March 6,2022 is {Access_count}")
print()

