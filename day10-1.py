import numpy as np
from collections import deque
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
grid = np.array([list(l) for l in lines])

START_SYMBOL = "L"

dist = np.zeros_like(grid, dtype=int) - 1
seen = np.zeros_like(grid, dtype=bool)

start_pos = np.where(grid == "S")
start_pos = start_pos[0][0], start_pos[1][0]
grid[start_pos] = START_SYMBOL
dist[start_pos] = 0
seen[start_pos] = True

q = deque([start_pos])
while len(q) > 0:
    cur = q.popleft()
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
        if not seen[i]:
            seen[i] = True
            dist[i] = dist[cur] + 1
            q.append(i)

print(np.max(dist))
