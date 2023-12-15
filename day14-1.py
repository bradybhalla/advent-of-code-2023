import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
lines = [list(l) for l in lines]

for c in range(len(lines[0])):
    move_to = 0
    for r in range(len(lines)):
        if lines[r][c] == "O":
            lines[r][c] = "."
            lines[move_to][c] = "O"
            move_to += 1
        elif lines[r][c] == "#":
            move_to = r + 1

total = 0
for r in range(len(lines)):
    for c in range(len(lines[0])):
        total += (len(lines) - r) if lines[r][c] == "O" else 0
print(total)
