from collections import deque
import numpy as np

with open("input.txt", "r") as f:
    s = f.read().strip()


def filter_digits(s):
    res = []
    new_needed = True
    for i in s:
        if i.isdigit():
            if new_needed:
                res.append("")
            res[-1] += i
            new_needed = False
        else:
            new_needed = True
    return res


lines = s.split("\n")

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(c)
    grid.append(row)

grid = np.array(grid)

arounds = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
connected = np.zeros_like(grid, dtype=float)


def fill_from(r, c):
    queue = deque([(r, c)])
    seen = set()
    seen.add((r, c))
    while len(queue) > 0:
        nr, nc = queue.pop()
        connected[nr, nc] = 1
        for dr, dc in arounds:
            if (
                nr + dr >= 0
                and nr + dr < len(grid)
                and nc + dc >= 0
                and nc + dc < len(grid[0])
            ):
                if not (nr + dr, nc + dc) in seen:
                    seen.add((nr + dr, nc + dc))
                    if grid[nr + dr][nc + dc] != ".":
                        queue.appendleft((nr + dr, nc + dc))


starts = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if not grid[i][j].isdigit() and not grid[i][j] == ".":
            fill_from(i, j)

grid[connected == 0] = "."

grid = grid.tolist()

total = 0
for i in grid:
    total += sum([int(i) for i in filter_digits("".join(i))])
print(total)
