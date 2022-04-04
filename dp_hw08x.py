#!/usr/bin/env python3
"""
Homework 08
    Write a universal launcher program that expects its command line
    arguments to consist of the absolute path to an executable program
    in any language, followed by any number of arguments for that
    program (e.g., /bin/ls -l). The wrapper should transparently run
    that program and exit with its exit value.
"""
import subprocess
import sys

# If no arguments exit with usage message.
if len(sys.argv) == 1:
    msg = 'usage: ' + str(sys.argv[0]) + ' path_to_executable [options]'
    sys.exit(msg)

# Using PIPE to capture standard error for python 3.5 and up (hills).
launched_process = subprocess.run(sys.argv[1:], stderr=subprocess.PIPE)

# Show standard error message and update exit code if not 0.
if launched_process.returncode != 0:
    print(launched_process.stderr.decode(), end='')
    sys.exit(launched_process.returncode)
