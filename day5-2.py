import numpy as np

with open("input.txt", "r") as f:
    s = f.read().strip()

lines = s.split("\n")
lines.append("")

seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
seeds = [(seeds[i], seeds[i]+seeds[i+1]-1) for i in range(0, len(seeds), 2)]
map_vals = []
i = 3
while i < len(lines):
    if lines[i] == "":
        new_seeds = []
        while len(seeds) > 0:
            seed_start, seed_end = seeds.pop()
            done = False
            for dst_start, src, l in map_vals:
                src_start, src_end = src, src+l-1
                map_delta = dst_start - src_start
                
                if seed_end < src_start or seed_start > src_end:
                    continue
                elif src_start <= seed_start and seed_end <= src_end:
                    new_seeds.append((seed_start + map_delta, seed_end + map_delta))
                    done = True
                    break
                elif src_start <= seed_end <= src_end:
                    seeds.append((seed_start, src_start-1))
                    new_seeds.append((src_start + map_delta, seed_end + map_delta))
                    done = True
                    break
                elif src_start <= seed_start <= src_end:
                    new_seeds.append((seed_start + map_delta, src_end + map_delta))
                    seeds.append((src_end+1, seed_end))
                    done = True
                    break
                elif seed_start <= src_start and src_end <= seed_end:
                    new_seeds.append((src_start + map_delta, src_end + map_delta))
                    seeds.append((seed_start, src_start-1))
                    seeds.append((src_end+1, seed_end))
                    done = True
                    break

            if not done:
                new_seeds.append((seed_start, seed_end))


        seeds = new_seeds
        map_vals = []

        i += 2
    else:
        map_vals.append(list(map(int, lines[i].split(" "))))
        i += 1

print(min(seeds)[0])
