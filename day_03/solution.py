#!/usr/bin/env python
# coding: utf-8

from functools import reduce
from operator import mul

PATH = 'input.txt'

def read_file(path):
    lst = []
    with open(path) as f:
        for line in f:
            lst.append(line[:-1])
    return lst

def travel(planet_matrix, move_right, move_down):
    pos_x = 0
    pos_y = 0
    width = len(planet_matrix[0])
    
    count = 0
    while pos_x < len(planet_matrix):
        terrain = planet_matrix[pos_x][pos_y % width]
        if terrain == '#':
            count += 1
        pos_x += move_down
        pos_y += move_right

    return count

def solve(moves):
    planet_matrix = read_file(PATH)
    return reduce(mul, [travel(planet_matrix, *move) for move in moves]) 

if __name__ == "__main__":
    print(solve([(3,1)]))
    print(solve([(1, 1), (3, 1), (5, 1), (7,1), (1,2)]))