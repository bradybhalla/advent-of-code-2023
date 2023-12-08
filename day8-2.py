import numpy as np
from functools import reduce
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")

inst = lines[0]

d = {}
starts = []
for i in lines[2:]:
    things = re.findall(r"(\w+) = \((\w+), (\w+)\)", i)[0]
    d[things[0]] = (things[1], things[2])
    if things[0][-1] == "A":
        starts.append(things[0])


def get_len(s):
    total = 0
    while True:
        for i in inst:
            s = d[s][0] if i == "L" else d[s][1]
            total += 1
            if s[-1] == "Z":
                return total


res = reduce(lambda x, y: np.lcm(x, y), [get_len(s) for s in starts])
print(res)
