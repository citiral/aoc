import sys
import json
from functools import reduce, cmp_to_key


def process_line(field, sx, sy, ex, ey):
    field[(sx, sy)] = '#'
    while sx != ex or sy != ey:
        if ex > sx:
            sx += 1
        elif ex < sx:
            sx -= 1
        if ey > sy:
            sy += 1
        elif ey < sy:
            sy -= 1
        field[(sx, sy)] = '#'


def process_path(path, field):
    parts = path.strip().split(" -> ")
    for i in range(len(parts)-1):
        sx, sy = map(int, parts[i].split(","))
        ex, ey = map(int, parts[i+1].split(","))
        process_line(field, sx, sy, ex, ey)


def calc_void(field):
    void = {}
    for val in field:
        x, y = val
        if x in void:
            void[x] = max(void[x], y + 1)
        else:
            void[x] = y + 1
    return void


def spawn(field, void, spawnx, spawny):
    x, y = spawnx, spawny

    while True:
        if not x in void or void[x] <= y:
            return False
        
        if (x, y+1) not in field:
            y += 1
        elif (x-1, y+1) not in field:
            x -= 1
            y += 1
        elif (x+1, y+1) not in field:
            x += 1
            y += 1
        else:
            field[(x, y)] = 'o'
            return True


def visualize(field, sx, ex, sy, ey):
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            if (x, y) in field:
                print(field[x, y], end='')
            else:
                print('.', end='')
        print()


def run1(lines):
    field = {}
    for path in lines:
        process_path(path, field)
    void = calc_void(field)
    print(void)
    visualize(field, 494, 503, 0, 9)
    spawned = 0
    while spawn(field, void, 500, 0):
        visualize(field, 494, 503, 0, 9)
        spawned += 1
    return spawned


def spawn2(field, floor_height, spawnx, spawny):
    x, y = spawnx, spawny

    while True:
        if (x, y) in field:
            return False
        
        if y+1 == floor_height:
            field[(x, y)] = '0'
            return True
        
        if (x, y+1) not in field:
            y += 1
        elif (x-1, y+1) not in field:
            x -= 1
            y += 1
        elif (x+1, y+1) not in field:
            x += 1
            y += 1
        else:
            field[(x, y)] = 'o'
            return True

def run2(lines):
    field = {}
    for path in lines:
        process_path(path, field)
    floor_height = max(y for _, y in field) + 2
    visualize(field, 494, 503, 0, 9)
    spawned = 0
    while spawn2(field, floor_height, 500, 0):
        #visualize(field, 494, 503, 0, 9)
        spawned += 1
    return spawned


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = list(map(str.strip, f.readlines()))
        print(run2(lines))