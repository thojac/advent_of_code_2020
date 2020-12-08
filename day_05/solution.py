#!/usr/bin/env python
# coding: utf-8

PATH = 'input.txt'

def read_input(PATH):
    data = []
    with open(PATH) as f:
        for line in f:
            data.append((line[:7], line[-4:-1])) # (row_id, col_id)
    return data

def classify_seat(seat_id):
    classifier = lambda seq, pred: sum(2**idx for idx, letter in enumerate(reversed(seq)) if letter == pred)
    return classifier(seat_id[0], 'B') * 8 + classifier(seat_id[1], 'R')

def solve_pt1():
    return max(classify_seat(bpass) for bpass in read_input(PATH))

def solve_pt2():
    passes = [classify_seat(bpass) for bpass in read_input(PATH)] 
    passes.sort()
    for idx, (a,b) in enumerate(zip(passes[:-1], passes[1:])):
        if b-a > 1:
            return a+1

print(solve_pt1())
print(solve_pt2())