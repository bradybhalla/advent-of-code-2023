with open("input.txt", "r") as f:
    s = f.read().strip()

lines = [[i for i in j if i.isdigit()] for j in s.split("\n")]
lines = [int(f"{j[0]}{j[-1]}") for j in lines]
print(sum(lines))

