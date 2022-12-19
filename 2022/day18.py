import sys


def get_neighbors(p, width):
    x, y, z, = p
    if x >= 0:
        yield (x-1, y, z)
    if y >= 0:
        yield (x, y-1, z)
    if z >= 0:
        yield (x, y, z-1)
    if x <= width:
        yield (x+1, y, z)
    if y <= width:
        yield (x, y+1, z)
    if z <= width:
        yield (x, y, z+1)


def floodfill(x, y, z, width, lava: set) -> set:
    remaining = [(x, y, z)]
    filled = set()

    while len(remaining) > 0:
        p = remaining.pop()
        

        if p in filled:
            continue
        else:
            filled.add(p)
            it = get_neighbors(p, width)

            n = next(it, None)
            while n != None:
                if n not in filled and n not in lava:
                    remaining.append(n)
                n = next(it, None)
    return filled


def invert(size: int, filled: set) -> set:
    r = set()
    for x in range(size+1):
        for y in range(size+1):
            for z in range(size+1):
                if (x, y, z) not in filled:
                    r.add((x, y, z))
    return r


def run1(lines):
    lava = set()
    
    covered_sides = 0
    for line in lines:
        x, y, z = [int(p) for p in line.strip().split(",")]
    
        lava.add((x, y, z))

        if (x-1, y, z) in lava:
            covered_sides += 2
        if (x+1, y, z) in lava:
            covered_sides += 2
        if (x, y-1, z) in lava:
            covered_sides += 2
        if (x, y+1, z) in lava:
            covered_sides += 2
        if (x, y, z-1) in lava:
            covered_sides += 2
        if (x, y, z+1) in lava:
            covered_sides += 2
    
    return len(lava) * 6 - covered_sides


def run2(lines):
    lava = set()
    
    for line in lines:
        x, y, z = [int(p) for p in line.strip().split(",")]
        lava.add((x, y, z))
    
    width = max(max(p) for p in lava)
    
    outside_air = floodfill(-1, -1, -1, width, lava)
    inside_lava = invert(width, outside_air)
    lava = set()
    
    covered_sides = 0
    for x, y, z in inside_lava:    
        lava.add((x, y, z))
        if (x-1, y, z) in lava:
            covered_sides += 2
        if (x+1, y, z) in lava:
            covered_sides += 2
        if (x, y-1, z) in lava:
            covered_sides += 2
        if (x, y+1, z) in lava:
            covered_sides += 2
        if (x, y, z-1) in lava:
            covered_sides += 2
        if (x, y, z+1) in lava:
            covered_sides += 2
    
    return len(lava) * 6 - covered_sides



if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        print(run2(lines))