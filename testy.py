#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework XX: Task:
 Write a program that .
"""

print('this is testy')

test_lst = [
    'a',
    'bb',
    'not',
    'abcba',
    'aabbccdccbbaa',
    'stillnot',
    '',
    '12321'
]  # test_lst has: trival 2, strict 3

PATH = "test_hw01.txt"

def safe_open(path):
    with open(path, 'r') as file_reader:
        return file_reader.readlines()


for line in safe_open(PATH):
    line = line.strip()
    if len(line) < 1:
        print(line + ' is 0 characters')
        continue
    elif len(line) == 1:
        print (line + ' is 1 character')
    elif len(line) == 2:
        print (line + ' is 2 characters')
    else:
        print (line + ' is 3 or more characters')
