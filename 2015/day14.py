import sys
import itertools


def tick(reindeer):
    if reindeer['running']:
        reindeer['distance'] += reindeer['speed']

    reindeer['tick'] += 1
    if reindeer['running'] and reindeer['tick'] == reindeer['stamina']:
        reindeer['running'] = False
        reindeer['tick'] = 0
    elif not reindeer['running'] and reindeer['tick'] == reindeer['rest']:
        reindeer['running'] = True
        reindeer['tick'] = 0

def run1(inp):
    reindeer = []

    for line in inp:
        values = line.strip().split()
        name = values[0]
        speed = int(values[3])
        stamina = int(values[6])
        rest = int(values[-2])
        reindeer.append({
            'name': name,
            'speed': speed,
            'stamina': stamina,
            'rest': rest,
            'running': True,
            'tick': 0,
            'distance': 0,
            'score': 0
        })
    
    for i in range(2503):
        for r in reindeer:
            tick(r)

        best = max([deer['distance'] for deer in reindeer])
        for deer in reindeer:
            if deer['distance'] == best:
                deer['score'] += 1

    return max([deer['score'] for deer in reindeer])

if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))