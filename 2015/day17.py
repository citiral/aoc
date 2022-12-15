import sys
import itertools

cache = {}

def fill(path, containers, liters, multipliers, multiplier):
    hashed = " ".join(map(str, path))
    if hashed in cache:
        return cache[hashed] * multiplier

    if liters == 0:
        cache[hashed] = multiplier
        return multiplier
    
    s = 0
    for c in containers:
        if c <= liters:
            containers2 = containers.copy()
            containers2.remove(c)
            s += fill(path + [c], containers2, liters - c, multipliers, multiplier * multipliers[c])
    cache[hashed] = s
    return s


def run1(inp):
    containers = [int(w.strip()) for w in inp]
    desired = 150
    
    count = 0
    mincount = len(containers)+1

    for i in range(1, len(containers)-1):
        for comb in itertools.combinations(containers, i):
            s = sum(comb)

            if s != desired:
                continue

            l = len(comb)
            if l < mincount:
                mincount = l
                count = 1
            elif l == mincount:
                count += 1
    
    return count


if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))
        print(cache)