import sys


def matches(expected, t, v):
    if t == "cats" or t == "trees":
        return expected[t] < v
    elif t == "pomeranians" or t == "goldfish":
        return expected[t] > v
    else:
        return expected[t] == v


def run1(inp):
    expected = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    for line in inp:
        values = line.strip().split()
        index = int(values[1][:-1])
        t1 = values[2][:-1]
        v1 = int(values[3][:-1])
        t2 = values[4][:-1]
        v2 = int(values[5][:-1])
        t3 = values[6][:-1]
        v3 = int(values[7])

        if matches(expected, t1, v1) and matches(expected, t2, v2) and matches(expected, t3, v3):
            print(index)


if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))