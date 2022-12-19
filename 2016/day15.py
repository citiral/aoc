import sys


def disc_iter(count, start):
    while True:
        yield start
        start += count


def are_equal(values):
    for i in range(1, len(values)):
        if values[0] != values[i]:
            return False
    return True

def run1(inp):
    discs = []

    for i in range(len(inp)):
        parts = inp[i].strip().split()
        count = int(parts[3])
        start = int(parts[-1][:-1])
        discs.append((count, (count - start - i - 1)%count))
    
    iters = []
    values = []
    for disc in discs:
        iter = disc_iter(disc[0], disc[1])
        iters.append(iter)
        values.append(next(iter))

    while not are_equal(values):
        m = min(values)
        for i in range(len(iters)):
            if values[i] == m:
                values[i] = next(iters[i])
    
    return values[0]


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))