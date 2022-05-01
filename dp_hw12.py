#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 12: Task:
    Write a CSV-to-JSON translator that expects the path to a CSV file
    as argument, and for each line in the file, prints out
    a JSON object encapsulating that record.
"""
import sys
import csv
import json

# If no file argument exit with usage message.
if len(sys.argv) == 1:
    msg = 'Usage: ' + str(sys.argv[0]) + ' CSV_FILE'
    sys.exit(msg)

# Parse csv file into dict objects then pretty print with json.dumps.
try:
    with open(sys.argv[1], encoding='utf-8') as csv_file:
        for record in csv.DictReader(csv_file):
            print(json.dumps(record, indent=4))

# Catch file/IO errors and exit gracefully.
except (FileNotFoundError, IOError):
    sys.exit('Unable to open file')
