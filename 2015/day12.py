import sys
import json
import collections.abc


def run1(inp):
    data = json.loads(inp[0])
    
    sum = 0
    todo = []
    todo.append(data)
    
    while len(todo) > 0:
        j = todo.pop()
        if isinstance(j, int):
            sum += j
        elif isinstance(j, str):
            continue
        elif isinstance(j, collections.abc.Sequence):
            for v in j:
                todo.append(v)
        elif isinstance(j, collections.abc.Mapping):
            skip = False
            for v in j:
                if j[v] == "red":
                    skip = True
            
            if not skip:
                for v in j:
                    todo.append(j[v])
    
    return sum

if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))