#!/usr/bin/env python3
"""
Homework 11:
    Write a program that expects as arguments any number of pathnames
    of UTF-8 encoded files, and indicates the mean number of
    bytes per character in the content of each one.
"""
import os
import sys


def mean_bpc(filename):
    """
    Takes in filename, returns mean bytes per character.
    """
    with open(filename, encoding='utf-8') as file:
        character_count = sum(len(line) for line in file)
        byte_count = os.path.getsize(filename)
        return byte_count / character_count


# Show results of running each argument through mean_bpc function.
for filepath in sys.argv[1:]:
    print('The file', filepath,
          'has a mean bytes per character of',
          round(mean_bpc(filepath), 3))
