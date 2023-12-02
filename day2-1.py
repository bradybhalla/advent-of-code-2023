import numpy as np

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")

def process(s):
    things = s.split(", ")
    extracted = []
    for i in things:
        sp = i.split(" ")
        extracted.append((int(sp[0]), sp[1]))
    return extracted

ids = []
games = []
for i in lines:
    l = i.split(": ")
    ids.append(int(l[0].split(" ")[1]))
    games.append([process(j) for j in l[1].split("; ")])

def is_valid(game):
    for s in game:
        for n,c in s:
            if c == "blue" and n > 14:
                return False
            elif c == "green" and n > 13:
                return False
            elif c == "red" and n>12:
                return False
    return True

total = 0
for id, game in zip(ids, games):
    if is_valid(game):
        total += id

print(total)
