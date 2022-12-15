import sys
import itertools


def score(p, weights):
    s = 0
    for i in range(len(p)):
        a = p[i-1]
        b = p[i]
        s += weights[a][b] + weights[b][a]
    return s


def run1(inp):
    weights = {'me': {}}

    for line in inp:
        values = line.strip().split()
        a = values[0]
        b = values[-1][:-1]
        change = int(values[3])
        if values[2] == "lose":
            change = -change

        if a not in weights:
            weights[a] = {'me': 0}
        weights[a][b] = change
    
    people = [person for person in weights] + ['me']
    for person in people:
        weights['me'][person] = 0
    print(weights)
    possibilities = itertools.permutations(people)
    

    bestScore = 0
    bestPoss = None
    for possibility in possibilities:
        s = score(possibility, weights)
        if bestPoss == None or s > bestScore:
            bestScore = s
            bestPoss = possibility
    
    return bestScore, bestPoss

if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))