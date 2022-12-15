import sys
import astar
import itertools

def look_and_say(s):
    r = ""
    cur = None
    count = 0
    for c in s:
        if cur == None:
            cur = c
            count = 1
        elif cur == c:
            count += 1
        else:
            r += str(count) + cur
            cur = c
            count = 1
    r += str(count) + cur
    return r


def run1(inp):
    val = inp[0].strip()

    for i in range(50):
        val = look_and_say(val)
    return len(val)

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.readlines()
        print(run1(inp))