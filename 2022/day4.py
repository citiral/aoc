import sys

def parse_pair(p):
    v1, v2 = p.split("-")
    return [int(v1), int(v2)]

def run1(lines):
    pairs = 0
    for line in lines:
        p1, p2 = [parse_pair(l) for l in line.strip().split(",")]
        if p1[1] >= p2[0] and p1[0] <= p2[1]:
            pairs += 1
    print(pairs)
    

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        run1(lines)