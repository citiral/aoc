import sys
import astar
import itertools

char_straits = set()
pairs = set()
disallowed = set(['i', 'o', 'ls'])

def is_valid(p):
    for d in disallowed:
        if d in p:
            return False

    fail = True
    for strait in char_straits:
        if p.find(strait) != -1:
            fail = False
            break
    if fail:
        return False
    
    for a in pairs:
        if p.find(a) != -1:
            for b in pairs:
                if a == b:
                    continue
                if p.find(b) != -1:
                    return True
    return False


def inc(c):
    v = ord(c)
    if v < ord('z'):
        return chr(v+1), False
    else:
        return 'a', True


def get_next(p):
    r = [c for c in p]

    for i in range(1, len(r)+1):
        v, cont = inc(r[-i])
        r[-i] = v
        if not cont:
            break
    return "".join(r)


def run1(inp):
    print(inp[0].strip(), get_next(inp[0].strip()))
    for line in inp:
        line = line.strip()
        p = line

        while not is_valid(p):
            p = get_next(p)
        print(line, "->", p)

def init():
    for i in range(26-2):
        offset = ord('a')
        s = chr(offset+i) + chr(offset+i+1) + chr(offset+i+2)
        char_straits.add(s)
    
    for i in range(26):
        offset = ord('a')
        s = chr(offset+i) + chr(offset+i)
        pairs.add(s)


if __name__ == "__main__":
    init()
    print(char_straits)
    print(pairs)
    with open(sys.argv[1], "r") as f:
        inp = f.readlines()
        run1(inp)