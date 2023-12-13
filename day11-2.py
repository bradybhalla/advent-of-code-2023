import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
lines = [list(l) for l in lines]


grid = np.zeros((len(lines), len(lines[0])))
grid[np.where(np.array(lines) == "#")] = 1

empty_cols = np.where(np.sum(grid, axis=0) == 0)[0]
empty_rows = np.where(np.sum(grid, axis=1) == 0)[0]

galaxies = np.where(grid == 1)


def calc_dist(r1, c1, r2, c2):
    total = abs(r1 - r2) + abs(c1 - c2)
    for i in range(min(r1, r2), max(r1, r2)):
        if i in empty_rows:
            total += 10**6-1

    for i in range(min(c1, c2), max(c1, c2)):
        if i in empty_cols:
            total += 10**6-1
    return total


total = 0
for i in range(len(galaxies[0])):
    for j in range(i):
        total += calc_dist(
            galaxies[0][i], galaxies[1][i], galaxies[0][j], galaxies[1][j]
        )
print(total)
