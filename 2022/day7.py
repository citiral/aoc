import sys


def process_sizes(fs):
    total_size = 0

    for f in fs:
        if f == '..size':
            total_size += fs[f]
        elif f == '..':
            continue
        else:
            size = process_sizes(fs[f])
            total_size += size
    
    fs['..size'] = total_size
    return total_size


def calc_sizes(fs):
    count = 0
    for f in fs:
        if f == '..size' or f == '..':
            continue
        count += calc_sizes(fs[f])
    if fs['..size'] <= 100000:
        count += fs['..size']
    return count


def calc_optimal(fs, free, required):
    optimal = 999999999999999
    if free + fs['..size'] >= required:
        optimal = fs['..size']
        print(optimal)
    for f in fs:
        if f == '..size' or f == '..':
            continue
        optimal = min(optimal, calc_optimal(fs[f], free, required))
    return optimal

def run1(lines):
    fs = {}
    fs['..'] = fs
    dir = fs
    for line in lines:
        if line[0] == '$':
            if line.startswith("$ cd"):
                if line[5] == '/':
                    dir = fs
                elif line[5:7] == '..':
                    dir = dir['..']
                else:
                    d = line[5:].strip()
                    if d not in dir:
                        dir[d] = {
                            '..': dir
                        }
                    dir = dir[d]
        elif line.startswith("dir"):
            continue
        else:
            size = int(line.split()[0])
            if not '..size' in dir:
                dir['..size'] = size
            else:
                dir['..size'] += size
    process_sizes(fs)

    free = 70000000 - fs['..size']
    required = 30000000
    return calc_optimal(fs, free, required)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        print(run1(lines))