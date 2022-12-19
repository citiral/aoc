import sys
import itertools

def run1(inp):
    nodes = []

    for line in inp[2:]:
        parts = line.strip().split()

        pos = parts[0].split("-")[1:]
        x = int(pos[0][1:])
        y = int(pos[1][1:])
        used = int(parts[2][:-1])
        avail = int(parts[3][:-1])
        print(used, avail)
        nodes.append((used, avail))

    pairs = itertools.permutations(nodes, 2)

    count = sum([1 if (a[0] > 0 and a[0] <= b[1]) else 0 for a, b in pairs])
    return count


def print_grid(nodes):
    for y in range(31):
        for x in range(34):
            n = nodes[(x, y)]
            if x == 0 and y == 0:
                print("S", end='')
            elif x == 33 and y == 0:
                print("G", end='')
            elif n[0] == 0:
                print("_", end='')
            elif n[0] + n[1] > 100:
                print("#", end='')
            else:
                print(".", end='')
        print()

def run2(inp):
    nodes = {}

    for line in inp[2:]:
        parts = line.strip().split()

        pos = parts[0].split("-")[1:]
        x = int(pos[0][1:])
        y = int(pos[1][1:])
        used = int(parts[2][:-1])
        avail = int(parts[3][:-1])
        nodes[(x, y)] = (used, avail)

    print_grid(nodes)
    print([nodes[a] for a in nodes if nodes[a][1] >= 70])

    return


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = f.readlines()
        print(run2(inp))