#!/usr/bin/env python
# coding: utf-8

import itertools
from functools import reduce

FILE_PATH = 'input.txt'

def read_file(path):
    lst = []
    with open(path) as f:
        for line in f:
            lst.append(int(line))
    return lst

def solver(r):
    numbers = read_file(FILE_PATH)
    for comb in itertools.combinations(numbers, r):
        if sum(comb) == 2020:
            return reduce(lambda x, y: x * y, comb)
    return 0

# Part 1
print(solver(2))

# Part 2
print(solver(3))


