#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 08: Task:
    Write a universal launcher program that expects its command line
    arguments to consist of the absolute path to an executable program
    in any language, followed by any number of arguments for that
    program (e.g., /bin/ls -l). The wrapper should transparently run
    that program and exit with its exit value
"""
import subprocess
import sys

# Shortest solution, next add argparse
p = subprocess.run(sys.argv[1:])
sys.exit(p.returncode)
