import sys

def handle_input(h, dir):
    if dir == 'U':
        h = (h[0] + 1, h[1])
    elif dir == 'D':
        h = (h[0] - 1, h[1])
    elif dir == 'L':
        h = (h[0], h[1] - 1)
    elif dir == 'R':
        h = (h[0], h[1] + 1)
    return h

def do_move(h, t):
    if abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1:
        return t
    
    if h[0] == t[0]:
        if t[1] == h[1] - 2:
            t = (t[0], t[1]+1)
        else:
            t = (t[0], t[1]-1)
    elif h[1] == t[1]:
        if t[0] == h[0] - 2:
            t = (t[0]+1, t[1])
        else:
            t = (t[0]-1, t[1])
    else:
        if h[0] > t[0]:
            t = (t[0]+1, t[1])
        else:
            t = (t[0]-1, t[1])
        if h[1] > t[1]:
            t = (t[0], t[1]+1)
        else:
            t = (t[0], t[1]-1)
    
    return t

def run1(lines):
    head = (0, 0)
    tail = (0, 0)
    print(head, tail)
    visited = set()
    visited.add(tail)

    for line in lines:
        dir, count = line.strip().split(" ")
        count = int(count)
        for i in range(count):
            head = handle_input(head, dir)
            tail = do_move(head, tail)
            visited.add(tail)
    
    return len(visited)

def run2(lines):
    rope = [(0, 0) for i in range(10)]
    visited = set()
    visited.add(rope[-1])

    for line in lines:
        dir, count = line.strip().split(" ")
        count = int(count)
        for i in range(count):
            rope[0] = handle_input(rope[0], dir)
            for i in range(len(rope) - 1):
                rope[i+1] = do_move(rope[i], rope[i+1])
            visited.add(rope[-1])
    
    return len(visited)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        print(run2(lines))