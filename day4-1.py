import numpy as np

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")


def process_line(i):
    while "  " in i:
        i = i.replace("  ", " ")
    v = i.split(": ")[1]
    v = v.split(" | ")
    return [int(i) for i in v[0].split(" ")], [int(i) for i in v[1].split(" ")]


total = 0
for i in lines:
    score = 0
    wins, nums = process_line(i)
    for j in nums:
        if j in wins:
            score = 1 if score == 0 else score * 2
    total += score

print(total)
