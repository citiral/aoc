import sys


def handle_exclude(range, begin, end):
    new_range = []
    for r in range:
        r_begin, r_end = r

        if begin > r_end or end < r_begin:
            new_range.append((r_begin, r_end))
        elif begin <= r_begin and end >= r_end:
            continue
        else:
            if begin > r_begin:
                new_range.append((r_begin, begin-1))
            if end < r_end:
                new_range.append((end+1, r_end))
    return new_range
            
        


def run1(inp):
    range = [(0, 4294967295)]

    for line in inp:
        begin, end = line.strip().split("-")
        range = handle_exclude(range, int(begin), int(end))
    
    return sum([r[1] - r[0] + 1 for r in range])


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))