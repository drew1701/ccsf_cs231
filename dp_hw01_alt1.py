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

import os.path
import sys


def fuzzy_path(ispath):
    if os.path.exists(ispath):
        return ispath
    return r'/users/abrick/resources/' + ispath


def safe_open_readlines(trypath):
    try:
        with open(fuzzy_path(trypath), 'r') as file_reader:
            return file_reader.readlines()
    except IOError:
        print('File can not be opened')
        sys.exit()


def increment_trivial(dict_object):
    dict_object['trivial'] += 1


def increment_strict(dict_object):
    dict_object['strict'] += 1


def is_pair_same(current, index):
    return current[index] == current[len(current)-1-index]


def is_palindrome(this_line):
    first = this_line[:len(this_line)//2]
    last = this_line[:len(this_line)//2:-1]
    if first == last:
        return True
    return False


def find_palindromes(test_file):
    for line in test_file:
        line = line.strip()
        if len(line) < 1:
            continue
        elif len(line) == 1:
            increment_trivial(palindromes)
        elif len(line) == 2:
            if is_pair_same(line, 0):
                increment_trivial(palindromes)
            else:
                continue
        elif is_palindrome(line):
            increment_strict(palindromes)


file_name = 'english'

palindromes = {
    "trivial": 0,
    "strict": 0
}

good_path = fuzzy_path(file_name)
find_palindromes(safe_open_readlines(good_path))

print('\nA palindrome is a word that reads the same forward and backward.')
print('Palindromes of <3 characters are sometimes called trivial.')
print('The file ' + good_path)
print('has a total of ' + str(sum(palindromes.values())) + ' palindromes.')
print(str(palindromes['trivial']) + ' are trivial in length, ' +
      str(palindromes['strict']) + ' are at lest 3 characters.\n')
if is_palindrome(str(sum(palindromes.values()))):
    print('The total number of palindromes is a palindrome.\n')
