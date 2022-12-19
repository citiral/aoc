import sys
import astar


number = 1364

def is_empty(x, y):
    v = x*x + 3*x + 2*x*y + y + y*y + number
    r = 1

    while v > 0:
        if v & 1 == 1:
            r = 1-r
        v = v >> 1
    
    return r


def get_neighbors(p):
    x, y = p

    if x > 0 and is_empty(x-1, y):
        yield (x-1, y)
    if y > 0 and is_empty(x, y-1):
        yield (x, y-1)
    if is_empty(x+1, y):
        yield (x+1, y)
    if is_empty(x, y+1):
        yield (x, y+1)


def run1(inp):
    a = astar.find_path((1, 1), (31, 39), get_neighbors, False, lambda a, b: b[0] - a[0] + b[1] - a[1], lambda x, y: 1)
    return len(list(a)) - 1


def run2(inp):
    visited = set()
    remaining = set([(1, 1)])

    for i in range(51):
        next = set()
        print(remaining)
        for location in remaining:
            visited.add(location)
            x, y = location

            if x > 0 and is_empty(x-1, y) and (x-1, y) not in visited:
                next.add((x-1, y))
            if y > 0 and is_empty(x, y-1) and (x, y-1) not in visited:
                next.add((x, y-1))
            if is_empty(x+1, y) and (x+1, y) not in visited:
                next.add((x+1, y))
            if is_empty(x, y+1) and (x, y+1) not in visited:
                next.add((x, y+1))
        remaining = next
    return len(visited)


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = [l.strip().split() for l in f.readlines()]
        print(run2(inp))