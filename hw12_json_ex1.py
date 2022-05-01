#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 12: Task:
    Write a CSV-to-JSON translator that expects the path to a CSV file
    as argument, and for each line in the file, prints out
    a JSON object encapsulating that record.
"""
import json

# {key:value mapping}
a = {"name": "John",
     "age": 31,
     "Salary": 25000,
     "this, that": "value"}

b = {
    1: "1,2,3",
    2: "4,5,6",
    3: "7,8,9"
}

# conversion to JSON done by dumps() function
out1 = json.dumps(a)
out2 = json.dumps(b)


# printing the output
print(out1)
print(out2)
