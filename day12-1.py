import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
lines = [re.split(r"\s+", l) for l in lines]

def get_counts(s):
    res = []
    inside = False
    for i in s:
        if i == "." or i == "?":
            inside = False
        elif i == "#":
            if not inside:
                res.append(0)
            inside = True
            res[-1] += 1
    return tuple(res)

def process(s, nums):
    res = 0
    nums = tuple([int(i) for i in nums.split(",")])
    questions = s.count("?")
    for i in range(2**questions):
        test = s
        for _ in range(questions):
            test = test.replace("?", "." if i%2 == 1 else "#", 1)
            i //= 2

        if nums == get_counts(test):
            res += 1
        

    return res

total = 0
for i in lines:
    total += process(*i)
print(total)
