import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n\n")
lines = [[list(i) for i in l.split("\n")] for l in lines]
num_lines = len(lines)

grids = []
for i in lines:
    grids.append(np.array(i))

def find_symmetry(grid):
    total = 0
    rows = ["".join(i) for i in grid]
    for i in range(1,len(rows)):
        left = i-1
        right = i
        works = True
        while left >= 0 and right < len(rows):
            if rows[left] != rows[right]:
                works = False
            left -= 1
            right += 1
        
        if works:
            total += 100*i


    rows = ["".join(i) for i in grid.T]
    for i in range(1,len(rows)):
        left = i-1
        right = i
        works = True
        while left >= 0 and right < len(rows):
            if rows[left] != rows[right]:
                works = False
            left -= 1
            right += 1
        
        if works:
            total += i

    return total


total = 0
for i in grids:
    total += find_symmetry(i)
print(total)
