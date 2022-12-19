import sys


def parse_blueprint(line):
    parts = line.split()

    return {
        "id": int(parts[1][:-1]),
        "costs" : [
            [int(parts[6]), 0, 0, 0],
            [int(parts[12]), 0, 0, 0],
            [int(parts[18]), int(parts[21]), 0, 0],
            [int(parts[27]), 0, int(parts[30]), 0],
        ]
    }


global_best = 0
cache = {}


def step_blueprint(bp, remaining, robots, ores, target):
    global global_best
    global_best = max(global_best, ores[3] + robots[3] * remaining)

    hash = f"{remaining}{robots}{ores}{target}"
    if hash in cache:
        #print("loading from cache")
        return cache[hash]

    if global_best > ores[3] + robots[3] * remaining + (robots[3]+remaining) * remaining/2:
        cache[hash] = global_best
        return global_best

    if remaining == 0:
        cache[hash] = ores[3]
        return ores[3]

    else:
        while True:
            can_purchase = True
            for i in range(4):
                if ores[i] < bp["costs"][target][i]:
                    can_purchase = False
            remaining -= 1
            for i in range(len(ores)):
                ores[i] += robots[i]
            if remaining <= 0:
                return ores[3]
            if can_purchase:
                break

        robots[target] += 1
        for i in range(4):
            ores[i] -= bp["costs"][target][i]

        best = 0
        for i in range(3, -1, -1):
            best = max(best, step_blueprint(bp, remaining, robots.copy(), ores.copy(), i))
        cache[hash] = best
        return best


def run1(lines):
    global global_best, cache
    blueprints = []

    for line in lines:
        blueprints.append(parse_blueprint(line.strip()))

    result = 0
    for bp in blueprints:
        print(bp, end='', flush=True)
        geode_count = 0
        cache = {}
        global_best = 0
        geode_count = step_blueprint(bp, 25, [0, 0, 0, 0], [bp["costs"][0][0], 0, 0, 0], 0)
        print(f" {geode_count}")
        result += geode_count * bp['id']
    return result


def run2(lines):
    global global_best, cache
    blueprints = []

    for line in lines[:3]:
        blueprints.append(parse_blueprint(line.strip()))

    result = 1
    for bp in blueprints:
        print(bp, end='', flush=True)
        cache = {}
        global_best = 0
        geode_count = step_blueprint(bp, 33, [0, 0, 0, 0], [bp["costs"][0][0], 0, 0, 0], 0)
        print(f" {geode_count}")
        result *= geode_count
    return result



if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        print(run2(lines))