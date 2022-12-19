import sys


shapes = [
    {
        'width': 4,
        'height': 1,
        'data': ["####"]
    },
    {
        'width': 3,
        'height': 3,
        'data': [".#.", "###", ".#."]
    },
    {
        'width': 3,
        'height': 3,
        'data': ["..#", "..#", "###"]
    },
    {
        'width': 1,
        'height': 4,
        'data': ["#", "#", "#", "#"]
    },
    {
        'width': 2,
        'height': 2,
        'data': ["##", "##"]
    },
]


def create_line():
    return [False for x in range(7)]


def is_empty(line):
    for cell in line:
        if cell:
            return False
    return True


def spawn_shape(level, shape_index):
    shape = shapes[shape_index]

    lowest_empty = -1
    for i in range(len(level)-1, -1, -1):
        if is_empty(level[i]):
            lowest_empty = i
        else:
            break
    
    return 2, lowest_empty+3+shape['height']-1



def print_level(level):
    for i in range(len(level)-1, -1, -1):
        row = level[i]
        print('|', end ='')
        for col in row:
            print('@' if col else '.', end='')
        print(f'| {i}')
    print("+-------+")


def intersects(level, shape, x, y):
    if x < 0 or y - shape['height'] + 1 < 0 or x + shape['width'] > 7:
        return True

    for sx in range(shape['width']):
        for sy in range(shape['height']):
            if level[y-sy][x+sx] and shape['data'][sy][sx] == '#':
                return True

    return False


def apply_shape(level, shape, x, y):
    for sx in range(shape['width']):
        for sy in range(shape['height']):
            level[y-sy][x+sx] |= shape['data'][sy][sx] == '#'


def get_height(level):
    for i in range(len(level)-1, -1, -1):
        if not is_empty(level[i]):
            return i+1

def run1(lines):
    gusts = lines[0].strip()
    level = [create_line(), create_line()]
    gust_index = 0
    shape_index = 0

    heights = [0]
    increases = [0]

    for i in range(100000):
        x, y = spawn_shape(level, shape_index)
        
        while y >= len(level):
            level.append(create_line())
        
        while True:
            g = gusts[gust_index]
            if g == '<' and not intersects(level, shapes[shape_index], x-1, y):
                x -= 1
            elif g == '>' and not intersects(level, shapes[shape_index], x+1, y):
                x += 1
            gust_index = (gust_index+1)%len(gusts)
            
            if intersects(level, shapes[shape_index], x, y-1):
                apply_shape(level, shapes[shape_index], x, y)
                shape_index = (shape_index+1)%len(shapes)
                break
            else:
                y -= 1
        
        heights.append(get_height(level))
        increases.append(heights[-1] - heights[-2])

    return increases


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        print(run1(lines))