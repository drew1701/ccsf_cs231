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

R_PATH = r'english'
# R_PATH = r'/users/abrick/resources/english'

palindrome = {
    "trivial": 0,
    "strict": 0
}


def safe_open(trypath):
    with open(trypath, 'r') as file_reader:
        return file_reader.readlines()


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
        print(line)
        if len(line) < 1:
            continue
        elif len(line) == 1:
            print('adding to trivial = ' + line)
            increment_trivial(palindrome)
        elif len(line) == 2:
            if is_pair_same(line, 0):
                increment_trivial(palindrome)
                print('adding to trivial = ' + line)
            else:
                continue
        elif check_all_pairs(line):
            print('adding to strict = ' + line)
            increment_strict(palindrome)
        # print('end of for loop')


# Call Functions
find_palindromes(safe_open(R_PATH))

print('A palindrome is a word that reads the same forward and backward.')
print('Palindromes of less than 3 characters are considered "trivial" \n'
      'in some circles')
