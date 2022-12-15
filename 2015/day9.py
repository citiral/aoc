import sys
import astar
import itertools

def calc_cost(path, distances):
    cost = 0
    prev = None
    for v in path:
        if prev != None:
            cost += distances[prev][v]
        prev = v
    return cost

def run1(inp):
    distances = {}
    for line in inp:
        line = line.strip()

        parts = line.split(" ")
        begin = parts[0]
        end = parts[2]
        cost = int(parts[-1])
        if begin not in distances:
            distances[begin] = {}
        if end not in distances:
            distances[end] = {}
        distances[begin][end] = cost
        distances[end][begin] = cost
    
    places = [begin for begin in distances]
    bestCost = 0
    for path in itertools.permutations(places):
        bestCost = max(calc_cost(path, distances), bestCost)
    return bestCost

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.readlines()
        print(run1(inp))