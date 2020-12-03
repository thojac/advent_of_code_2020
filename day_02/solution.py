#!/usr/bin/env python
# coding: utf-8

import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

PATH = 'input.txt'

def process_line(line):
    data =  re.split('\s|-', line.replace(':', ''))[:-1]
    data[0] = int(data[0])
    data[1] = int(data[1])
    return data

def check_1(minn, maxx, key, password):
    count = password.count(key)
    return 1 if (count >= minn and count <= maxx) else 0

def check_2(minn, maxx, key, password):
    check = sum([password[minn-1] == key, password[maxx-1] == key])
    return 1 if check == 1 else 0

def solve(check):
    lines = read_file(PATH, dtype=str)
    count = 0
    for idx, line in enumerate(lines):
        count += check(*process_line(line))
    return count

if __name__ == "__main__":
    print(solve(check_1))
    print(solve(check_2))

