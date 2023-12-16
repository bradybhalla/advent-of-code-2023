import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

things = s.split(",")

# id, focal len
boxes = [[] for _ in range(256)]

for s in things:
    s_id = s.split("=")[0].split("-")[0]
    curr = 0
    for i in s_id:
        curr += ord(i)
        curr *= 17
        curr %= 256

    if "-" in s:
        id = s[:-1]
        boxes[curr] = [i for i in boxes[curr] if i[0] != id]
    elif "=" in s:
        id, fl = s.split("=")
        matches = [i for i in range(len(boxes[curr])) if boxes[curr][i][0] == id]
        contains, index = len(matches) > 0, sum(matches)

        if contains:
            boxes[curr][index] = (id, fl)
        else:
            boxes[curr].append((id, fl))

total = 0
for box_num, box in enumerate(boxes):
    for slot_num, slot in enumerate(box):
        total += (box_num+1)*(slot_num+1)*int(slot[1])
print(total)


