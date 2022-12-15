import sys

def run1(lines):
    res = 0
    for line in lines:
        dims = line.strip().split("x")
        l, w, h = [int(v) for v in dims]
        a = 2*l*w
        b = 2*w*h
        c = 2*h*l
        res += a + b + c + int(min([a, b, c])/2)
    return res

def run2(lines):
    res = 0
    for line in lines:
        dims = line.strip().split("x")
        l, w, h = [int(v) for v in dims]
        ribbon = min(2*l+2*w, 2*w+2*h, 2*l+2*h)
        bow = l*w*h
        print(ribbon, bow)
        res += ribbon + bow
    return res

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.readlines()

        print(run2(inp))