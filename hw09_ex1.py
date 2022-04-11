#!/usr/bin/env python3
# Demonstrate race condition with many unsafe calls.
# 1000 workers do busywork and decrement a counter;
# results differ almost every time.
import os, threading


def unsafe():
    global value
    found = value
    with open(os.devnull, 'w') as null:
        busywork = print(found*str(found),file=null)
    value = found - 1


value = 10**3
for _ in range(value):
    threading.Thread(target=unsafe).start()
print(value)
