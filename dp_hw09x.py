#!/usr/bin/env python3
"""
Homework 09
    Write a program that expects pathnames as arguments and
    creates a pool of workers to all at once count
    how many lines long each file is.
"""
import os
import sys
from multiprocessing import Pool


def check_exists(files_list):
    """
    Takes in list, returns list of files found with os.path.exists.
    """
    good_list = []
    for line in files_list:
        if os.path.exists(line):
            good_list.append(line)
    return good_list


def count_lines(filename):
    """
    Takes in filename, returns filename and count of lines.
    """
    with open(filename, 'r') as file_handler:
        num_lines = sum(1 for line in file_handler)
    msg = filename + ' has ' + str(num_lines) + ' lines.'
    return msg


if __name__ == '__main__':

    # Very simple error checking.
    safe_list = check_exists(sys.argv[1:])
    # If no good files exit with usage message.
    if len(safe_list) == 0:
        usage = 'Usage: ' + str(sys.argv[0]) + ' FILE1 [FILE2...]'
        sys.exit(usage)

    # Create Pool of workers.
    p = Pool()
    result = p.map(count_lines, safe_list)

    # Show results on separate lines.
    print(*result, sep='\n')

    # Shut down the Pool of workers.
    p.close()
    p.join()
