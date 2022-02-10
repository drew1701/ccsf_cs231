#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 01: Task:
    Write a program that prints the number of palindromes in
    /users/abrick/resources/english
Notes:
    Will count palindromes <3 digits as trivial, larger as strict
"""

R_PATH = r'test_hw01.txt'
# R_PATH = r'english'
# R_PATH = r'/users/abrick/resources/english'

palindrome = {
    "trivial": 0,
    "strict": 0
}


def safe_open(path):
    with open(path) as file_reader:
        return file_reader.readlines()


def is_pair_same(current, index):
    return current[index] == current[len(current)-1-index]


def find_max_first(current):
    if len(current) % 2 == 0:
        return len(current)//2
    else:
        return len(current)//2-1


def check_all_pairs(this_line):
    for index in range(find_max_first(this_line)):
        if not is_pair_same(this_line, index):
            return False
    return True


def increment_trivial(dict_object):
    dict_object['trivial'] += 1


def increment_strict(dict_object):
    dict_object['strict'] += 1


def find_palindromes(test_file):
    for line in test_file:
        if len(line) < 1:
            continue
        elif len(line) == 1:
            increment_trivial(palindrome)
        elif len(line) == 2 and is_pair_same(line, 1):
            increment_trivial(palindrome)
        elif check_all_pairs(line):
            increment_strict(palindrome)

# Call Functions
this_file = safe_open(R_PATH)
find_palindromes(this_file)
print(palindrome)