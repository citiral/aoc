import sys


def parse_valve(line):
    s = line.strip().split()

    connections = []
    for i in range(len(s)-9):
        if i < len(s)-10:
            connections.append(s[i+9][:-1])
        else:
            connections.append(s[i+9])
    valve = {
        'id': s[1],
        'rate': int(s[4][5:-1]),
        'connections': connections
    }

    return valve


def calc_distance_matrix(valves):
    dm = {}
    for id in valves:
        v = valves[id]
        dm[(v['id'], v['id'])] = 0
        for c in v['connections']:
            dm[(v['id'], c)] = 1
    
    changed = False
    appends = []
    while True:
        changed = False
        for c1 in dm:
            for c2 in dm:
                if c1[1] == c2[0]:
                    c3 = (c1[0], c2[1])
                    if c3 not in dm or dm[c1] + dm[c2] < dm[c3]:
                        changed = True
                        appends.append((c3, dm[c1] + dm[c2]))
        for append in appends:
            dm[append[0]] = append[1]
        if not changed:
            break
    return dm


def search_optimal(valves, dm, remaining, current, closed, released):
    if len(closed) == 0:
        return released
    else:
        best = released
        for valve in closed:
            dist = dm[(current, valve)]
            gain = (remaining-dist-1) * valves[valve]['rate']
            if remaining-dist-1 > 0:
                best = max(best, search_optimal(valves, dm, remaining-dist-1, valve, closed.difference([valve]), released+gain))
        return best


#global_best = 2492
global_best = 0
global_best_path = None


def update_global_best(score, pos1, pos2, closed):
    global global_best, global_best_path
    if score > global_best:
        global_best = score
        global_best_path = (pos1, pos2, closed)
        print(global_best_path, score)


def calc_heuristic(valves, dm, p1, p2, closed, remaining):
    a = sorted([(valves[a]['rate'], a) for a in closed], reverse=True)
    result = 0
    for i in range(len(a)):
        d = min(dm[(p1, a[i][1])], dm[(p2, a[i][1])])
        result += max(0, (remaining-int(i/2) - d)) * valves[a[i][1]]['rate']
    return result 


def search_optimal_2(valves, dm, remaining, pos1, pos2, visited1, visited2, closed, released):
    update_global_best(released, pos1, pos2, closed)
    nv1 = visited1.union([pos1])
    nv2 = visited2.union([pos2])
    global global_best
    if len(closed) == 0 or remaining == 0:
        return released
    elif global_best >= calc_heuristic(valves, dm, pos1, pos2, closed, remaining) + released:
        return released
    else:
        best = released
        if pos1 in closed and pos2 in closed and pos1 != pos2:
            gain1 = (remaining-1) * valves[pos1]['rate']
            gain2 = (remaining-1) * valves[pos2]['rate']
            best = max(best, search_optimal_2(valves, dm, remaining-1, pos1, pos2, set(), set(), closed.difference([pos1, pos2]), released+gain1+gain2))

        if pos1 in closed:
            gain = (remaining-1) * valves[pos1]['rate']
            for dest in valves[pos2]['connections']:
                if dest in visited2 or pos2 in visited2:
                    continue
                best = max(best, search_optimal_2(valves, dm, remaining-1, pos1, dest, set(), nv2, closed.difference([pos1]), released+gain))
            best = max(best, search_optimal_2(valves, dm, remaining-1, pos1, pos2, set(), nv2, closed.difference([pos1]), released+gain))

        if pos2 in closed and pos1 != pos2:
            gain = (remaining-1) * valves[pos2]['rate']
            for dest in valves[pos1]['connections']:
                if dest in visited1 or pos1 in visited1:
                    continue
                best = max(best, search_optimal_2(valves, dm, remaining-1, dest, pos2, nv1, set(), closed.difference([pos2]), released+gain))
            best = max(best, search_optimal_2(valves, dm, remaining-1, pos1, pos2, nv1, set(), closed.difference([pos2]), released+gain))

        targs1 = [pos1]
        if pos1 not in visited1:
            targs1.extend(valves[pos1]['connections'])
        targs2 = [pos2]
        if pos2 not in visited2:
            targs2.extend(valves[pos2]['connections'])
        
        for dest1 in targs1:
            if dest1 != pos1 and dest1 in visited1:
                continue
            for dest2 in targs2:
                if dest2 != pos2 and dest2 in visited2:
                    continue
                best = max(best, search_optimal_2(valves, dm, remaining-1, dest1, dest2, nv1, nv2, closed, released))
        return best


def run1(lines):
    valves = {}
    for line in lines:
        v = parse_valve(line)
        valves[v['id']] = v

    dm = calc_distance_matrix(valves)
    return search_optimal(valves, dm, 30, 'AA', set([valves[v]['id'] for v in valves if valves[v]['rate'] > 0]), 0)



def run2(lines):
    global global_best
    valves = {}
    for line in lines:
        v = parse_valve(line)
        valves[v['id']] = v

    dm = calc_distance_matrix(valves)

    #for i in range(27):
    i = 26
    print(f"searching {i}: ")
    print(search_optimal_2(valves, dm, i, 'AA', 'AA', set(), set(), set([valves[v]['id'] for v in valves if valves[v]['rate'] > 0]), 0))
    print(global_best)
    print(global_best_path)
    return global_best


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        print(run2(lines))