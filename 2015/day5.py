import sys
import regex
import hashlib

vowels = set("aeiou")
disallowed = set(["ab", "cd", "pq", "xy"])

def run1(inp):
    count = 0
    for line in inp:
        line = line.strip()
        vowelcount = len([v for v in line if v in vowels])
        if vowelcount < 3:
            continue
        double = False
        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                double = True
                break
        if not double:
            continue
        fail = False
        for v in disallowed:
            print(line, v, line.find(v))
            if line.find(v) >= 0:
                fail = True
        if fail:
            continue
        count += 1

    return count


def run2(inp):
    count = 0
    for line in inp:
        if regex.search(r"^.*(?P<a>..).*(?P=a).*$", line) == None:
            continue
        if regex.search(r"^.*(?P<a>.).(?P=a).*$", line) == None:
            continue
        count += 1
    return count


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.readlines()
        print(run2(inp))