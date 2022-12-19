import sys
import astar
import hashlib


def is_open(c):
    return c in "bcdef"

def get_neighbors(p):
    h = hashlib.md5(p[2].encode()).hexdigest()

    if p[1] > 0 and is_open(h[0]):
        yield (p[0], p[1] - 1, p[2] + "U")
    if p[1] < 3 and is_open(h[1]):
        yield (p[0], p[1] + 1, p[2] + "D")
    if p[0] > 0 and is_open(h[2]):
        yield (p[0] - 1, p[1], p[2] + "L")
    if p[0] < 3 and is_open(h[3]):
        yield (p[0] + 1, p[1], p[2] + "R")

def run1(inp):
    passcode = inp[0].strip()
    path = astar.find_path((0, 0, passcode), (3, 3, ""), get_neighbors, False, lambda a, b: abs(b[0] - a[0]) + abs(b[1] - a[1]), lambda a, b: 1, lambda a, b: a[0] == b[0] and a[1] == b[1])

    return list(path)[-1][2][len(passcode):]


def longest_path(p):
    if p[0] == 3 and p[1] == 3:
        return len(p[2])
    else:
        it = get_neighbors(p)
        best = 0
        for neighbor in it:
            best = max(best, longest_path(neighbor))
        return best


def run2(inp):
    passcode = inp[0].strip()
    p = longest_path((0, 0, passcode))
    return p - len(passcode)


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = f.readlines()
        print(run2(inp))