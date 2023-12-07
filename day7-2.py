import numpy as np

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
hands = [i.split(" ") for i in lines]

def get_counts(hand):
    r = {}
    j_counts = 0
    for i in hand:
        if i == "J":
            j_counts += 1
        else:
            if i not in r:
                r[i] = 0
            r[i] += 1

    res = list(sorted([(k, v) for k,v in r.items()], key=lambda x: -x[1]))
    if len(res) == 0:
        res = [("J",5)]
    else:
        res[0] = (res[0][0], res[0][1]+j_counts)
    return res

CARDS = "J23456789TQKA"
def calc_key(hand1):
    counts = get_counts(hand1)
    if len(counts) == 1:
        c1 = [counts[0][1], 0]
    else:
        c1 = [get_counts(hand1)[0][1], get_counts(hand1)[1][1]]
    for i in hand1:
        c1.append(CARDS.index(i))
    return tuple(c1)


hands = list(sorted(hands, key=lambda x: calc_key(x[0])))

total = 0
for ind, (hand, bid) in enumerate(hands):
    total += int(bid)*(ind+1)
print(total)
