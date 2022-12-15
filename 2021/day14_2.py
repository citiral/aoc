import sys
from collections import Counter

def expand(polymer, rules):
    result = {}
    for rule in rules:
        if rule in polymer:
            count = polymer[rule]
            outp = rules[rule]

            m1 = rule[0] + outp
            m2 = outp + rule[1]
            
            if m1 in result:
                result[m1] = count + result[m1]
            else:
                result[m1] = count
            if m2 in result:
                result[m2] =  count + result[m2]
            else:
                result[m2] = count
    return result

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        input = [l.strip() for l in f.readlines()]
        polymer_str = input[0]
        polymer = {}

        for i in range(len(polymer_str) - 1):
            v = polymer_str[i:i+2]
            if v in polymer:
                polymer[v] += 1
            else:
                polymer[v] = 1
        print(polymer)
        
        rules = {}
        for rule in input[2:]:
            (inp, out) = rule.split(" -> ")
            rules[inp] = out

        for i in range(40):
            polymer = expand(polymer, rules)
            print(polymer)

        counts = {}

        for v in polymer:
            (a, b) = v
            if not a in counts:
                counts[a] = polymer[v] / 2
            else:
                counts[a] += polymer[v] / 2
            if not b in counts:
                counts[b] = polymer[v] / 2
            else:
                counts[b] += polymer[v] / 2
            
        print(counts)
        v = counts.values()
        print(max(v) - min(v))