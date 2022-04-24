#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 09: Task:
    Write a program that expects pathnames as arguments and
    creates a pool of workers to all at once count
    how many lines long each file is.
"""
import os
import sys
from multiprocessing import Pool


def check_exists(files_list):
    good_list = []
    for line in files_list:
        if os.path.exists(line):
            good_list.append(line)
    return good_list


def count_lines(filename):
    with open(filename, 'r') as fp:
        num_lines = sum(1 for line in fp)
    msg = filename + ' has ' + str(num_lines) + ' lines.'
    print(msg)
    return msg


if __name__ == '__main__':

    safe_list = check_exists(sys.argv[1:])

    for file in safe_list:
        count_lines(file)
