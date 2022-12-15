import sys


def tick(cpu):
    x = cpu["x"]
    v = cpu["cycle"] % 40

    if x >= v-1 and x <= v+1:
        print("#", end='')
    else:
        print(".", end='')
    
    if v == 39:
        print()
    

    cpu["cycle"] += 1
    if (cpu["cycle"] + 20) % 40 == 0:
        v = cpu["x"] * cpu["cycle"]
        cpu["sum"] += v

def run1(lines):
    cpu = {
        "x": 1,
        "cycle": 0,
        "sum": 0
    }

    for line in lines:
        line = line.strip()
        if line == "noop":
            tick(cpu)
        else:
            add = int(line.split()[-1])
            tick(cpu)
            tick(cpu)
            cpu["x"] += add
    
    print()
    return cpu["sum"]

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        print(run1(lines))