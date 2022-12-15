import sys

def move(p, instr):
    x, y = p
    if instr == '>':
        return x+1, y
    elif instr == '<':
        return x-1, y
    elif instr == '^':
        return x, y+1
    elif instr == 'v':
        return x, y-1

def run1(inp):
    visited = set()

    santa = (0, 0)
    robot = (0, 0)
    visited.add((0, 0))
    santasTurn = True

    for v in inp:
        if santasTurn:
            santa = move(santa, v)
        else:
            robot = move(robot, v)
        santasTurn = not santasTurn
        visited.add(santa)
        visited.add(robot)
    return len(visited)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.readlines()
        print(run1(inp[0]))