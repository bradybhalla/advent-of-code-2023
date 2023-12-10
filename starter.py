import numpy as np
import re

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
lines = [re.split(r"\s+", l) for l in lines]
