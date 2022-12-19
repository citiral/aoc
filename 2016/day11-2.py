import sys
import itertools
import copy
import astar
import json


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


def hash(v):
    for i in range(len(v['floors'])):
        v['floors'][i] = sorted(v['floors'][i])
    return json.dumps(v, sort_keys=True)


def unhash(v):
    return json.loads(v)


def get_neighbors(v):
    v = unhash(v)
    elevator = v['e']
    floors = v['floors']
    for i in range(2, 0, -1):
        selections = itertools.permutations(floors[elevator], i)

        for selection in selections:
            if elevator > 0:
                f = copy.deepcopy(floors)
                f[elevator] = [item for item in floors[elevator] if item not in selection]
                f[elevator-1].extend(selection)
                if is_possible(f):
                    yield hash({'e': elevator-1, 'floors': f})
            if elevator < 3:
                f = copy.deepcopy(floors)
                f[elevator] = [item for item in floors[elevator] if item not in selection]
                f[elevator+1].extend(selection)
                if is_possible(f):
                    yield hash({'e': elevator+1, 'floors': f})


def heuristic_cost(a, goal):
    a = unhash(a)
    return 1
    #return len(a['floors'][0]) + len(a['floors'][1])*2 + len(a['floors'][2])*4 + len(a['floors'][3]*8)


def distance(a, b):
    return 1


def run1(inp):  
    #start = {'e': 0, 'floors': [['HM', 'LM'], ['HG'], ['LG'], []]}
    #end = {'e': 3, 'floors': [[], [], [], ['HM', 'LM', 'HG', 'LG']]}
    start = {'e': 0, 'floors': [['PG', 'SG'], ['PM', 'SM'], ['RG', 'RM', 'UG', 'UM'], []]}
    end = {'e': 3, 'floors': [[], [], [], ['PG', 'SG', 'PM', 'SM', 'RG', 'RM', 'UG', 'UM']]}
    #start = {'e': 0, 'floors': [['EG', 'EM', 'DG', 'DM', 'TG', 'TM', 'PG', 'SG'], ['PM', 'SM'], ['RG', 'RM', 'UG', 'UM'], []]}
    #end = {'e': 3, 'floors': [[], [], [], ['EG', 'EM', 'DG', 'DM', 'TG', 'TM', 'PG', 'SG', 'PM', 'SM', 'RG', 'RM', 'UG', 'UM']]}
    
    v = list(astar.find_path(hash(start), hash(end), get_neighbors, False, heuristic_cost, distance))
    for item in v:
        print(item)
    return len(v)-1


if __name__=="__main__":
    with open("day11.txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))