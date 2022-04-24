#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 10: Task:
    Decorate print() (by assignment, not the pie) so that
    each positional argument it receives has a 50% chance
    of being ignored, and demonstrate this behavior.
"""
# This never worked...

import functools
import subprocess
import builtins
import sys


def mod_print(func):
    @functools.wraps(func)
    def wrapper_mod_print(*args, **kwargs):
        wp = subprocess.run(print(*args, **kwargs), stdout=subprocess.PIPE)
        return wp.stdout.decode()
    return wrapper_mod_print()


def print(*args, **kwargs):
    return builtins.print(*args, **kwargs)


print = mod_print(print)

