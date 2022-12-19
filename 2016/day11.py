import sys
import itertools
import copy
import astar

desired = 10
searched = {}


def is_possible(floors):
    for f in floors:
        reactors = set()
        chips = set()
        for item in f:
            v = item[0]
            t = item[1]
            if t == 'G':
                reactors.add(v)
            else:
                chips.add(v)
        if len(reactors) > 0 and len(chips.difference(reactors)) > 0:
            return False
    return True

def search(floors, depth, elevator):
    for i in range(len(floors)):
        floors[i] = sorted(floors[i])

    s = str(floors)+f":{elevator}"
    
    if s in searched and searched[s] <= depth:
        return 999999
    else:
        searched[s] = depth
    
    if not is_possible(floors):
        return 999999
    
    if len(floors[-1]) == desired:
        return depth

    best = 999999
    
    for i in range(1, 3):
        selections = itertools.permutations(floors[elevator], i)

        for selection in selections:
            if elevator < 3:
                f = copy.deepcopy(floors)
                f[elevator] = [item for item in floors[elevator] if item not in selection]
                f[elevator+1].extend(selection)
                best = min(search(f, depth+1, elevator+1), best)
            if elevator > 0:
                f = copy.deepcopy(floors)
                f[elevator] = [item for item in floors[elevator] if item not in selection]
                f[elevator-1].extend(selection)
                best = min(search(f, depth+1, elevator-1), best)
        
    return best


def run1(inp):
    floors = [['TG', 'TM', 'PG', 'SG'], ['PM', 'SM'], ['RG', 'RM', 'UG', 'UM'], []]
    
    return search(floors, 0, 0)


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))