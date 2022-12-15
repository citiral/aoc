import sys
import json
from functools import reduce, cmp_to_key


def lesserThan(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 == l2:
            return None
        else:
            return l1 < l2
    
    elif isinstance(l1, int):
        return lesserThan([l1], l2)
    elif isinstance(l2, int):
        return lesserThan(l1, [l2])
    else:
        length1 = len(l1)
        length2 = len(l2)
        for i in range(min(len(l1), len(l2))):
            r = lesserThan(l1[i], l2[i])
            if r != None:
                return r

        if length1 == length2:
            return None
        return length1 < length2


def run1(lines):
    result = 0
    for i in range(int(len(lines)/3)+1):
        l1 = json.loads(lines[i*3])
        l2 = json.loads(lines[i*3+1])

        if lesserThan(l1, l2):
            result += (i+1)
            print(f"Pair {i} in order")
        else:
            print(f"Pair {i} not in order")
    return result


def compare(a, b):
    r = lesserThan(a, b)
    if r == None:
        return 0
    elif r == True:
        return -1
    else:
        return 1


def run2(lines):
    dec1 = [[2]]
    dec2 = [[6]]
    parsed = [dec1, dec2]
    for line in lines:
        if len(line.strip()) > 0:
            parsed.append(json.loads(line))
    
    data = sorted(parsed, key=cmp_to_key(compare))

    result = 1
    for i in range(len(data)):
        if data[i] == dec1 or data[i] == dec2:
            result *= (i+1)

    return result


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = list(map(str.strip, f.readlines()))
        print(run1(lines))