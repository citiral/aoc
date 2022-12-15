import sys

def get_memory_length(s):
    length = 0
    inSlash = False
    inStr = False
    for c in s:
        if inSlash:
            if c == '\\' or c == '"':
                inSlash = False
                length += 1
            elif c == 'x':
                inSlash = False
                length -= 1
        else:
            if c == '\\':
                inSlash = True
            elif c != '"':
                length += 1
    return length


def encode(s):
    res = ""

    for c in s:
        if c == '"':
            res += '\\"'
        elif c == '\\':
            res += '\\\\'
        else:
            res += c
    
    return f'"{res}"'


def run1(inp):
    count = 0
    for line in inp:
        line = line.strip()
        count += len(line) - get_memory_length(line)
    return count

def run2(inp):
    count = 0
    for line in inp:
        line = line.strip()
        print(line, encode(line))
        count += len(encode(line)) - len(line)
    return count

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.readlines()
        print(run2(inp))