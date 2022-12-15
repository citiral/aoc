import sys

def get_visible(x, y, dirx, diry, w, h, treeline):
    height = treeline[y][x]
    yield (x, y)
    while True:
        x += dirx
        y += diry

        if x < 0 or y < 0 or x >= w or y >= h:
            return

        next = treeline[y][x]
        if next > height:
            yield (x, y)
        height = max(next, height)


def get_senic(x, y, dirx, diry, w, h, treeline):
    height = treeline[y][x]
    count = 0
    
    while True:
        x += dirx
        y += diry

        if x < 0 or y < 0 or x >= w or y >= h:
            return count

        next = treeline[y][x]
        if next >= height:
            return count +1
        else:
            count += 1


def calc_senic(x, y, w, h, treeline):
    return  get_senic(x, y, 1, 0, w, h, treeline) *\
            get_senic(x, y, -1, 0, w, h, treeline) *\
            get_senic(x, y, 0, 1, w, h, treeline) *\
            get_senic(x, y, 0, -1, w, h, treeline)

def run1(lines):
    width = len(lines[0])
    height = len(lines)

    visible = set()

    for x in range(width):
        visible.update(get_visible(x, 0, 0, 1, width, height, lines))
        visible.update(get_visible(x, height-1, 0, -1, width, height, lines))
    for y in range(height):
        visible.update(get_visible(0, y, 1, 0, width, height, lines))
        visible.update(get_visible(width-1, y, -1, 0,  width, height, lines))
    
    for y in range(height):
        for x in range(width):
            if (y, x) in visible:
                print('#', end='')
            else:
                print(' ', end='')
        print() 

    return len(visible)

def run2(lines):
    width = len(lines[0])
    height = len(lines)

    best = None
    bestscore = -1

    for x in range(width):
        for y in range(height):
            s = calc_senic(x, y, width, height, lines)
            if s > bestscore:
                bestscore = s
                best = (y, x)
    
    return best, bestscore

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        lines = [[int(c) for c in line.strip()] for line in lines]
        print(run1(lines))