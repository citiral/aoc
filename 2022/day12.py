import sys
import astar


heightmap = []
width = 0
height = 0


def neighbors(v):
    x, y = v
    h = heightmap[y][x]

    if x > 0 and heightmap[y][x-1] <= h + 1:
        yield (x-1, y)
    if y > 0 and heightmap[y-1][x] <= h + 1:
        yield (x, y-1)
    if x < width-1 and heightmap[y][x+1] <= h + 1:
        yield (x+1, y)
    if y < height-1 and heightmap[y+1][x] <= h + 1:
        yield (x, y+1)


def distance(n1, n2):
    return 1


def cost(n, goal):
    return 1


def run1(inp):
    global heightmap
    global width
    global height
    width = len(inp[0].strip())
    height = len(inp)
    heightmap = [[0 for x in range(width)] for y in range(height)]
    start = (0, 0)
    end = (0, 0)
    
    for y in range(height):
        for x in range(width):
            c = inp[y][x]

            if c == 'S':
                start = (x, y)
                h = 0
            elif c == 'E':
                end = (x, y)
                h = 25
            else:
                h = ord(c) - ord('a')
            heightmap[y][x] = h
    
    best = 9999
    for y in range(height):
        for x in range(width):
            if heightmap[y][x] != 0:
                continue
            path = astar.find_path((x, y), end, neighbors_fnct=neighbors, heuristic_cost_estimate_fnct=cost, distance_between_fnct=distance)
            if path:
                best = min(best, len(list(path))-1)
    return best
        

if __name__=="__main__":
    with open(sys.argv[0][:-2]+"txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))
