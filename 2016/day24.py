import sys
import astar
import math
import itertools
from tqdm import tqdm

def distance(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    return math.sqrt(x*x + y*y)


def get_neighbors(map, a):
    x, y = a
    if x > 0 and map[y][x-1] != '#':
        yield (x-1, y)
    if y > 0 and map[y-1][x] != '#':
        yield (x, y-1)
    if x < len(map[0]) - 1 and map[y][x+1] != '#':
        yield (x+1, y)
    if y < len(map) - 1 and map[y+1][x] != '#':
        yield (x, y+1)
    


pathcache = {}
def path_from(map, start, end):
    if (start, end) in pathcache:
        return pathcache[(start, end)]
    elif (end, start) in pathcache:
        return pathcache[(end, start)]

    path = astar.find_path(start, end, lambda a: get_neighbors(map, a), False, lambda a, b: distance(a, b), lambda a, b: 1)

    pathcache[(start, end)] = len(list(path)) - 1
    pathcache[(end, start)] = pathcache[(start, end)]
    return pathcache[(start, end)]


def node_counts(map):
    count = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] != '#' and map[y][x] != ".":
                count += 1
    return count


def find_node(map, node):
    c = str(node)
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == c:
                return (x, y)
    return None


def calculate_length(map, path):
    nodes = [0]
    nodes.extend(path)
    nodes.append(0)
    length = 0
    for i in range(len(nodes)-1):
        length += path_from(map, find_node(map, nodes[i]), find_node(map, nodes[i+1]))
    return length

def run1(map):
    node_count = node_counts(map)

    orders = itertools.permutations(range(1, node_count))

    best = 99999
    for path in tqdm(list(orders)):
        best = min(best, calculate_length(map, path))
    return best


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = [l.strip() for l in f.readlines()]
        print(run1(inp))