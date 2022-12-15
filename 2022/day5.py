import sys

def parse_pair(p):
    v1, v2 = p.split("-")
    return [int(v1), int(v2)]

def do_move(stack, count, begin, end):
    popped = stack[begin][-count:]
    stack[begin] = stack[begin][:-count]
    stack[end] += popped

def run1(lines):
    parsing_stacks = True
    stack_count = int((len(lines[0]) + 1) / 4)
    stacks = [[] for x in range(stack_count)]

    for i in range(len(lines)):
        line = lines[i]
        if parsing_stacks:
            for x in range(stack_count):
                c = line[x*4+1]
                if ord(c) >= ord('0') and ord(c) <= ord('9'):
                    parsing_stacks = False
                    print(stacks)
                    break
                elif c != ' ':
                    stacks[x].insert(0, c)
        else:
            line = line.strip()
            if line != '':
                s = line.split()
                amount, begin, end = int(s[1]), int(s[3]), int(s[5])
                do_move(stacks, amount, begin - 1, end - 1)
    
    print(stacks)

    for s in stacks:
        print(s[-1], end='')

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        run1(lines)