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


def check_all_pairs(this_line):
    for index in range(len(this_line)//2):
        if not is_pair_same(this_line, index):
            return False
    return True


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
        elif check_all_pairs(line):
            increment_strict(palindromes)


F_NAME = 'english'

palindromes = {
    "trivial": 0,
    "strict": 0
}

if __name__ == '__main__':
    good_path = fuzzy_path(F_NAME)
    find_palindromes(safe_open_readlines(good_path))

    print('\nA palindrome is a word that reads the same forward and backward.')
    print('Palindromes of <3 characters are sometimes called trivial.')
    print('The file ' + good_path)
    print('has a total of ' + str(sum(palindromes.values())) + ' palindromes.')
    print(str(palindromes['trivial']) + ' are trivial in length, ' +
          str(palindromes['strict']) + ' are at lest 3 characters.\n')
    if check_all_pairs(str(sum(palindromes.values()))):
        print('The total number of palindromes is a palindrome.\n')
