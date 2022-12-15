import sys
from collections import Counter

def expand(polymer, rules):
    output = ""
    for i in range(len(polymer) - 1):
        v = polymer[i:i+2]
        output += v[0]
        if v in rules:
            output += rules[v]
    output += polymer[-1]
    return output

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        input = [l.strip() for l in f.readlines()]
        polymer = input[0]
        rules = {}
        for rule in input[2:]:
            (inp, out) = rule.split(" -> ")
            rules[inp] = out

        for i in range(40):
            polymer = expand(polymer, rules)
        
        print(Counter(polymer))
        v = Counter(polymer).values()
        print(max(v) - min(v))