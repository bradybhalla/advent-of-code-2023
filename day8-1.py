import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")

inst = lines[0]

d = {}
for i in lines[2:]:
    things = re.findall(r"(\w+) = \((\w+), (\w+)\)", i)[0]
    d[things[0]] = (things[1], things[2])

curr = "AAA"
total = 0
while True:
    for i in inst:
        curr = d[curr][0] if i == "L" else d[curr][1]
        total += 1
    if curr == "ZZZ":
        break
print(total)
