import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
times = int("".join(re.split(r"\s+", lines[0])[1:]))
dists = int("".join(re.split(r"\s+", lines[1])[1:]))

def dist(time, record):
    total = 0
    for i in range(0, time):
        dist_traveled = i*(time - i)
        if dist_traveled > record:
            total += 1
    return total


print(dist(times, dists))
