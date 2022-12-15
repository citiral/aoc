import sys
import json
import math
from scanf import scanf

def parse(line):
    result = []
    for l in line.strip():
        if l == ',':
            continue
        elif l == '[' or l == ']':
            result.append(l)
        else:
            result.append(int(l))
    return result

def explode(line):
    depth = 0
    for i in range(len(line)):
        if line[i] == '[':
            depth += 1
        elif line[i] == ']':
            depth -= 1
        elif depth == 5:
            val_l = line[i]
            val_r = line[i+1]
            for x in range(i-1, -1, -1):
                if isinstance(line[x], int):
                    line[x] += val_l
                    break
            for x in range(i+2, len(line)):
                if isinstance(line[x], int):
                    line[x] += val_r
                    break
            return True, line[:i-1] + [0] + line[i+3:]
    return False, line


def split(line):
    for i in range(len(line)):
        if isinstance(line[i], int) and line[i] >= 10:
            l = math.floor(line[i] / 2)
            r = math.ceil(line[i] / 2)
            return True, line[:i] + ['[', l, r, ']'] + line[i+1:]
    return False, line

def reduce(line):
    exploded, result = explode(line)
    if exploded:
        return reduce(result)
    else:
        splitted, result = split(line)
        if splitted:
            return reduce(result)
        else:
            return result

def add(l, r):
    v = ['[']
    v.extend(l)
    v.extend(r)
    v.append(']')
    return reduce(v)

def magnitude(l):
    mag = 0
    curside = 'l'
    if len(l) == 4:
        return l[1] * 3 + l[2] * 2
    else:
        depth = 0

        if isinstance(l[1], int):
            mag += l[1] * 3
            curside = 'r'
        if isinstance(l[-2], int):
            mag += l[-2] * 2

        for i in range(len(l)):
            if l[i] == '[':
                depth += 1
                if depth == 2 and curside == 'r':
                    mag += magnitude(l[i:-1]) * 2
            elif l[i] == ']':
                depth -= 1
                if depth == 1 and curside == 'l':
                        mag += magnitude(l[1:i+1]) * 3
                        curside = 'r'
    return mag

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [parse(l) for l in f.readlines()]

        best_m = 0
        for i1 in range(len(lines)):
            for i2 in range(len(lines)):
                best_m = max(best_m, magnitude(add(lines[i1], lines[i2])))
        print(best_m)