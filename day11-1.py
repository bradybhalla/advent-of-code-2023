import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
lines = [list(l) for l in lines]


grid = np.zeros((len(lines), len(lines[0])))
grid[np.where(np.array(lines) == "#")] = 1

empty_cols = np.where(np.sum(grid, axis=0)==0)[0]
empty_rows = np.where(np.sum(grid, axis=1)==0)[0]
for i,j in enumerate(empty_cols):
    grid = np.insert(grid, j+i, 0, axis=1)
for i,j in enumerate(empty_rows):
    grid = np.insert(grid, j+i, 0, axis=0)

galaxies = np.where(grid == 1)

total = 0
for i in range(len(galaxies[0])):
    for j in range(i):
        total += abs(galaxies[0][i] - galaxies[0][j]) + abs(galaxies[1][i] - galaxies[1][j])
print(total)
