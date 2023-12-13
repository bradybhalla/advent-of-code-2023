import numpy as np
from collections import deque
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
grid = np.array([list(l) for l in lines])

START_SYMBOL = "L"

seen = np.zeros_like(grid, dtype=bool)

start_pos = np.where(grid == "S")
start_pos = start_pos[0][0], start_pos[1][0]
grid[start_pos] = START_SYMBOL
seen[start_pos] = True

path = [start_pos, (start_pos[0], start_pos[1]+1)]

while path[-1] != start_pos:
    cur = path[-1]
    neighbors = []
    if grid[cur] == "|":
        neighbors.append((cur[0] + 1, cur[1]))
        neighbors.append((cur[0] - 1, cur[1]))
    elif grid[cur] == "-":
        neighbors.append((cur[0], cur[1] + 1))
        neighbors.append((cur[0], cur[1] - 1))
    elif grid[cur] == "L":
        neighbors.append((cur[0] - 1, cur[1]))
        neighbors.append((cur[0], cur[1] + 1))
    elif grid[cur] == "J":
        neighbors.append((cur[0] - 1, cur[1]))
        neighbors.append((cur[0], cur[1] - 1))
    elif grid[cur] == "7":
        neighbors.append((cur[0] + 1, cur[1]))
        neighbors.append((cur[0], cur[1] - 1))
    elif grid[cur] == "F":
        neighbors.append((cur[0] + 1, cur[1]))
        neighbors.append((cur[0], cur[1] + 1))

    for i in neighbors:
        if i != path[-2] and i != path[-1]:
            path.append(i)
            break

area = 0
height = 0
for i in range(len(path)):
    p1 = path[i]
    p2 = path[(i+1)%len(path)]
    dr = p2[0] - p1[0]
    dc = p2[1] - p1[1]
    height += dr
    area += dc * height

print(int(abs(area) - len(path)/2 + 1.5))

