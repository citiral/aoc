import sys
import itertools


def make_field(w, h):
    return [[False for x in range(w)] for y in range(h)]


def count_neighbors(field, x, y):
    c = 0
    if x > 0 and field[y][x-1]:
        c += 1
    if y > 0 and field[y-1][x]:
        c += 1
    if x > 0 and y > 0 and field[y-1][x-1]:
        c += 1
    if x < len(field[0]) - 1 and field[y][x+1]:
        c += 1
    if y < len(field) - 1 and field[y+1][x]:
        c += 1
    if x < len(field[0]) - 1 and y < len(field) - 1 and field[y+1][x+1]:
        c += 1
    if x < len(field[0]) - 1 and y > 0 and field[y-1][x+1]:
        c += 1
    if y < len(field) - 1 and x > 0 and field[y+1][x-1]:
        c += 1
    return c


def run1(inp):
    width = len(inp[0])
    height = len(inp)

    field = make_field(width, height)

    for x in range(width):
        for y in range(height):
            field[y][x] = inp[y][x] == '#'
    
    field[0][0] = True
    field[height-1][0] = True
    field[0][width-1] = True
    field[height-1][width-1] = True

    for i in range(100):
        next_field = make_field(width, height)
        for x in range(width):
            for y in range(height):
                if  (x == 0 and y == 0) or\
                    (x == 0 and y == height-1) or\
                    (x == width-1 and y == 0) or\
                    (x == width-1 and y ==height-1):
                    next_field[y][x] = True
                    continue
                c = count_neighbors(field, x, y)
                if field[y][x]:
                    next_field[y][x] = c == 2 or c == 3
                else:
                    next_field[y][x] = c == 3
        field = next_field
    return sum([sum(l) for l in field])
    



if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = f.readlines()
        print(run1([l.strip() for l in inp]))