with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] + [
    str(i) for i in range(1, 10)
]

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_sum(l):
    first = ""
    for i in range(len(l)):
        for j in digits:
            if l[i : i + len(j)] == j:
                first = j
                break
        if first != "":
            break

    last = ""
    for i in range(len(l) - 1, -1, -1):
        for j in digits:
            if i + len(j) > len(l):
                continue
            if l[i : i + len(j)] == j:
                last = j
        if last != "":
            break

    return vals[digits.index(first)] * 10 + vals[digits.index(last)]


total = 0
for l in lines:
    total += get_sum(l)

print(total)
