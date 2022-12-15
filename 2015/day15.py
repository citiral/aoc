import sys


def get_score(vals, ing):
    cal = sum(ing[i][4] * vals[i] for i in range(len(vals)))
    if cal != 500:
        return 0
    cap = sum(ing[i][0] * vals[i] for i in range(len(vals)))
    dur = sum(ing[i][1] * vals[i] for i in range(len(vals)))
    fla = sum(ing[i][2] * vals[i] for i in range(len(vals)))
    tex = sum(ing[i][3] * vals[i] for i in range(len(vals)))

    return max(0, cap) * max(0, dur) * max(0, fla) * max(0, tex)


def run1(inp):
    ingredients = []

    for line in inp:
        values = line.strip().split()
        cap = int(values[2][:-1])
        dur = int(values[4][:-1])
        fla = int(values[6][:-1])
        tex = int(values[8][:-1])
        cal = int(values[10])
        ingredients.append((cap, dur, fla, tex, cal))
    

    bestScore = 0
    for i in range(101):
        for j in range(101-i):
            for k in range(101-i-j):
                for l in range(101-i-j-k):
                    bestScore = max(bestScore, get_score([i, j, k, l], ingredients))
    return bestScore


if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))