import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
lines = [re.split(r"\s+", l) for l in lines]


def get_matches(target, full_str):
    res = []
    for i in range(len(full_str) - len(target) + 1):
        substr = full_str[i : i + len(target)]
        if not any(
            [substr[j] != target[j] and substr[j] in "#." for j in range(len(target))]
        ):
            res.append(i)
        if full_str[i] == "#":
            break
    return res


def process(s, nums):
    nums = [int(i) for i in nums.split(",")] * 5
    s = "?".join([s for _ in range(5)])

    vals = [[0 for _ in range(len(nums) + 1)] for _ in range(len(s) + 1)]
    for i in range(len(s) + 1):
        vals[i][len(nums)] = int("#" not in s[i:])

    for i in reversed(range(len(s) + 1)):
        matches = get_matches("#" * nums[-1], s[i:])
        for j in matches:
            vals[i][len(nums) - 1] += vals[i + nums[-1] + j][len(nums)]

    for i in reversed(range(len(s) + 1)):
        for j in reversed(range(len(nums) - 1)):
            matches = get_matches("#" * nums[j] + ".", s[i:])
            for k in matches:
                vals[i][j] += vals[i + nums[j] + 1 + k][j + 1]

    return vals[0][0]


total = 0
for i in lines:
    total += process(*i)
print(total)
