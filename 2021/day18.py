import sys
import json
import math
from scanf import scanf

def get_depth(n):
    if isinstance(n, int):
        return 0
    else:
        return max(get_depth(n[0]), get_depth(n[1])) + 1

def get_max(n):
    if isinstance(n, int):
        return n
    else:
        return max(get_max(n[0]), get_max(n[1]))

def add(n, l, r):
    if l != None:
        if isinstance(n[0], int):
            n[0] += l
        else:
            add(n[0], l, r)
    elif r != None:
        if isinstance(n[1], int):
            n[1] += r
        else:
            add(n[1], l, r)

def explode(n, depth):
    if isinstance(n, int):
        return ('stop', None)
    if depth == 3 and not isinstance(n[0], int):
        v = n[0]
        n[0] = 0
        if isinstance(n[1], int):
            n[1] += v[1]
        else:
            add(n[1], v[1], None)
        return ('left', v[0])
    elif depth == 3 and not isinstance(n[1], int):
        v = n[1]
        n[1] = 0
        if isinstance(n[0], int):
            n[0] += v[0]
        else:
            add(n[0], None, v[1])
        return ('right', v[1])
    else:
        e = explode(n[0], depth+1)
        if e[0] == 'done':
            return e
        elif e[0] == 'left':
            return e
        elif e[0] == 'right':
            if isinstance(n[1], int):
                n[1] += e[1]
            else:
                add(n[1], e[1], None)
            return ('done', None)
        else:
            e = explode(n[1], depth+1)
            if e[0] == 'done':
                return e
            elif e[0] == 'right':
                return e
            elif e[0] == 'left':
                if isinstance(n[0], int):
                    n[0] += e[1]
                else:
                    add(n[0], None, e[1])
                return ('done', None)
            else:
                return e

def split(n):
    if isinstance(n, int):
        return False
    if isinstance(n[0], int) and n[0] >= 10:
        l = int(n[0]/2)
        n[0] = [l, n[0] - l]
        return True
    elif isinstance(n[1], int) and n[1] >= 10:
        l = int(n[1]/2)
        n[1] = [l, n[1] - l]
        return True
    elif split(n[0]):
        return True
    else:
        return split(n[1])

def process(n):
    if get_depth(n) > 4:
        explode(n, 0)
        #print(n)
        return process(n)
    elif get_max(n) >= 10:
        split(n)
        #print(n)
        return process(n)
    else:
        return n

def run1(lines):
    sum = lines[0]
    #process(sum)
    for line in lines[1:]:
        sum = [sum, line]
        #sprint(sum)
        process(sum)
        print(sum)
    return sum

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [json.loads(l.strip()) for l in f.readlines()]
        print(run1(lines))