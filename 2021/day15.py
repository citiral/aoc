import sys
import astar
from collections import Counter

map = []
width = 0
height = 0

def sample_map(x, y):
    wrap_x = int(x / width)
    wrap_y = int(y / height)

    score = map[y%height][x%width] + wrap_x + wrap_y
    return (score % 9) + 1

def neighbors(n):
    x, y = n
    if x > 0:
        yield (x-1, y)
    if y > 0:
        yield (x, y-1)
    if x < width*5 - 1:
        yield (x+1, y)
    if y < height*5 - 1:
        yield (x, y+1)

def distance(n1, n2):
    x, y = n2
    return sample_map(x, y)

def cost(n, goal):
    x, y = n
    return 1#goal[0] - x + goal[1] - y

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f.readlines()]
        for line in lines:
            map.append([int(i)-1 for i in line])
    
    width = len(map[0])
    height = len(map)

    path = list(astar.find_path((0, 0), (width*5-1, height*5-1), neighbors_fnct=neighbors,
                                heuristic_cost_estimate_fnct=cost, distance_between_fnct=distance))
    
    cost = 0
    for p in path[1:]:
        x, y = p
        cost += sample_map(x, y)
    print(cost)