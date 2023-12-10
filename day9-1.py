import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

def get_seqs(nums):
    vals = [nums]
    while True:
        vals.append([vals[-1][i]-vals[-1][i-1] for i in range(1,len(vals[-1]))])
        if sum(vals[-1]) == 0:
            break
    prev = 0
    for i in range(len(vals)):
        prev = vals[len(vals)-1-i][-1] + prev
    return prev

lines = s.split("\n")
lines = [list(map(int,re.split(r"\s+", l))) for l in lines]

print(sum([get_seqs(i) for i in lines]))

