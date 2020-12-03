#!/usr/bin/env python3

def read_file(path, dtype=int):
    lst = []
    with open(path) as f:
        for line in f:
            lst.append(dtype(line))
    return lst
