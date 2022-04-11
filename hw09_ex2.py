#!/usr/bin/env python3
# Functional calculation of ten logarithms by a pool of workers.
import concurrent.futures, math

inputs = range(1, 10)
pool = concurrent.futures.ThreadPoolExecutor()
print(list(zip(inputs, pool.map(math.log, inputs))))
