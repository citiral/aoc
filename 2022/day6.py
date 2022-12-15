import sys

def run1(lines):
    line = lines[0]

    for i in range(3, len(line)):
        s = set(line[i-14:i])
        if len(s) == 14:
            return i

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        print(run1(lines))