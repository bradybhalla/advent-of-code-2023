import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

things = s.split(",")

total = 0
for s in things:
    curr = 0
    for i in s:
        curr += ord(i)
        curr *= 17
        curr %= 256
    total += curr
print(total)

