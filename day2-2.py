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

def power(game):
    red = 0
    green = 0
    blue = 0
    for s in game:
        for n,c in s:
            if c == "blue":
                blue = max(blue, n)
            elif c == "green":
                green = max(green, n)
            elif c == "red":
                red = max(red, n)
    return red*green*blue

total = 0
for id, game in zip(ids, games):
    total += power(game)

print(total)
