from collections import deque
import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
lines = [list(l) for l in lines]


def get_load():
    total = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            total += (len(lines) - r) if lines[r][c] == "O" else 0
    return total


def cycle():
    for c in range(len(lines[0])):
        move_to = 0
        for r in range(len(lines)):
            if lines[r][c] == "O":
                lines[r][c] = "."
                lines[move_to][c] = "O"
                move_to += 1
            elif lines[r][c] == "#":
                move_to = r + 1

    for r in range(len(lines)):
        move_to = 0
        for c in range(len(lines[0])):
            if lines[r][c] == "O":
                lines[r][c] = "."
                lines[r][move_to] = "O"
                move_to += 1
            elif lines[r][c] == "#":
                move_to = c + 1

    for c in range(len(lines[0])):
        move_to = len(lines) - 1
        for r in reversed(range(len(lines))):
            if lines[r][c] == "O":
                lines[r][c] = "."
                lines[move_to][c] = "O"
                move_to -= 1
            elif lines[r][c] == "#":
                move_to = r - 1

    for r in range(len(lines)):
        move_to = len(lines[0]) - 1
        for c in reversed(range(len(lines[0]))):
            if lines[r][c] == "O":
                lines[r][c] = "."
                lines[r][move_to] = "O"
                move_to -= 1
            elif lines[r][c] == "#":
                move_to = c - 1


tail = 132
for i in range(tail):
    cycle()

test_length = 200
test_block = []
for i in range(test_length):
    cycle()
    test_block.append(get_load())

sliding_block = deque([-1 for i in range(test_length)])
counter = 0
while True:
    sliding_block.popleft()
    cycle()
    sliding_block.append(get_load())
    counter += 1

    if all([test_block[i] == sliding_block[i] for i in range(test_length)]):
        break

print(test_block[(1_000_000_000 - tail - 1) % counter])
