import sys
from enum import Enum


def parse_option(opt):
    if opt == 'A' or opt == 'X':
        return 0
    elif opt == 'B' or opt == 'Y':
        return 1
    else:
        return 2


def calc_score(p1, p2):
    if p1 == p2:
        return 4 + p2
    elif p2 == (p1 + 1) % 3:
        return p2 + 7
    else:
        return p2 + 1


def run(lines):
    score = 0
    for line in lines:
        v1, v2 = [opt for opt in line.split()]
        p1 = parse_option(v1)
        if v2 == 'X':
            p2 = (p1 - 1) % 3
        elif v2 == 'Y':
            p2 = p1
        else:
            p2 = (p1 + 1) % 3
        score += calc_score(p1, p2)
    print(score)
    

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        run(lines)