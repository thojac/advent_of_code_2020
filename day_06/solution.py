#!/usr/bin/env python
# coding: utf-8

from functools import reduce
import re

PATH = 'input.txt'

def process_input(PATH):
    with open(PATH) as f:
        raw = [group.split('\n') for group in re.split(r'\n\n', f.read())]
        return [{'sett': {letter for entry in group for letter in entry}, 
                 'count': reduce(lambda x,y: x & y,[{x for x in test} for test in group])} 
                for group in raw]

def solve_pt1():
    return sum(len(group['sett']) for group in process_input(PATH))

def solve_pt2():
    return sum(len(group['count']) for group in process_input(PATH))

print(solve_pt1())
print(solve_pt2())