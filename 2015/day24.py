import sys
import itertools


def quantum_entanglement(group):
    r = 1
    for item in group:
        r *= item
    return r


def can_be_divided(input, desired):
    for i in range(1, int(len(input) / 2)):
        for group in itertools.combinations(input, i):
            if sum(group) == desired:
                return True
    return False
 

def can_be_divided2(input, desired):
    for i in range(1, int(len(input) / 2)):
        for group in itertools.combinations(input, i):
            if sum(group) == desired and can_be_divided([i for i in input if i not in group], desired):
                return True
    return False


def run1(input):
    input = set(input)
    groupsize = int(sum(input) / 4)
    mingrouplength = int(len(input) / 4)

    best = None
    bestqe = None

    for i in range(1, mingrouplength+1):
        if best != None:
            break
        for group in itertools.combinations(input, i):
            if sum(group) != groupsize or not can_be_divided2([i for i in input if i not in group], groupsize):
                continue

            if best == None or len(group) < len(best) or quantum_entanglement(group) < bestqe:
                best = group
                bestqe = quantum_entanglement(group)
                print(best, bestqe)

    return best, bestqe


if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = [int(l) for l in f.readlines()]
        print(run1(inp))