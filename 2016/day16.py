import sys


def next_state(a):
    b = "".join(["1" if c == "0" else "0" for c in a[::-1]])
    return f"{a}0{b}"


def checksum(v):
    c = ""
    for i in range(0, len(v), 2):
        if v[i] == v[i+1]:
            c += "1"
        else:
            c += "0"
    if len(c) % 2 == 0:
        return checksum(c)
    else:
        return c


def run1(inp):
    desired_length = 35651584
    
    v = inp[0].strip()
    while len(v) < desired_length:
        v = next_state(v)
    v = v[:desired_length]

    check = checksum(v)
    return len(check), check


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))