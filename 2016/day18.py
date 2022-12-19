import sys

def next_line(line):
    newfield = [False for l in range(len(line))]

    for i in range(1, len(line)-1):
        if line[i-1] and line[i] and not line[i+1]:
            newfield[i] = True
        elif not line[i-1] and line[i] and line[i+1]:
            newfield[i] = True
        elif line[i-1] and not line[i] and not line[i+1]:
            newfield[i] = True
        elif not line[i-1] and not line[i] and line[i+1]:
            newfield[i] = True
    return newfield


def run1(inp):
    field = [[False]]
    field[0].extend([c == '^' for c in inp[0].strip()])
    field[0].append(False)
    for i in range(400000-1):
        field.append(next_line(field[-1]))
    
    safe = 0
    for line in field:
        safe += len(line) - sum(line) - 2
    return safe


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))