import numpy as np

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")

class Map():
    def __init__(self):
        self.vals = []

    def add_range(self, dst, src, l):
        self.vals.append((src, dst, l))

    def get_val(self, src):
        for s,d,l in self.vals:
            if s <= src < s+l:
                return d+(src-s)
        return src


seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
m = Map()
i = 3
while i < len(lines):
    if lines[i] == "":
        seeds = [m.get_val(j) for j in seeds]
        m = Map()
        i += 2
    else:
        m.add_range(*map(int, lines[i].split(" ")))
        i += 1

seeds = [m.get_val(j) for j in seeds]
print(min(seeds))

