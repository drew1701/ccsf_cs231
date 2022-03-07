#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 04: Task:
    Write a program that demonstrates a generator yielding the
    number of accesses made in each hour, from the beginning of
    /etc/httpd/logs/access_log
"""

from datetime import datetime
from datetime import timedelta


def count_hits_per_hour(number_of_hours):
    hour_count = 0
    is_first_line = True
    format_code = '%d/%b/%Y:%H:%M:%S'
    hits = 0
    while hour_count <= number_of_hours:
        line = file_handler.readline()
        line = line.partition('[')[2]
        line = line.partition(' -')[0]
        dt_object = datetime.strptime(line, format_code)
        time_tuple = dt_object.timetuple()

        if is_first_line:
            last_time_tuple = time_tuple
            current_hour = time_tuple[3]
            is_first_line = False

        if current_hour == time_tuple[3]:
            hits += 1
        elif time_tuple[2] == last_time_tuple[2] and time_tuple[3] > current_hour:
            print('hour', current_hour, ' total hits', hits)
            hour_count += 1
            hits = 1
            current_hour = time_tuple[3]
        elif time_tuple[2] > last_time_tuple[2]:
            print('hour', current_hour, ' total hits', hits)
            last_time_tuple = (dt_object + timedelta(days=1)).timetuple()
            hour_count += 1
            hits = 1
            current_hour = 0


file_path = 'access_log'
file_handler = open(file_path, 'r')
count_hits_per_hour(25)
file_handler.close()
