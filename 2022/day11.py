import sys
import math
from functools import reduce

globalMod = 0

def parse_item(i):
    if i[-1] == ',':
        return int(i[:-1])
    else:
        return int(i)


def parse_monkey(input):
    monkey = {}
    
    monkey['id'] = input[0].split()[1][:-1]
    monkey['items'] = []
    items = input[1].split()[2:]
    for item in items:
        monkey['items'].append(parse_item(item))
    monkey['operation'] = input[2][17:]
    monkey['test'] = int(input[3].split()[3])
    monkey['true'] = int(input[4].split()[-1])
    monkey['false'] = int(input[5].split()[-1])
    monkey['inspected'] = 0
    return monkey


def resolve(operation, old):
    parts = operation.split()
    v1 = old
    v2 = old if parts[2] == 'old' else int(parts[2])

    if parts[1] == '+':
        return v1 + v2
    elif parts[1] == '*':
        return v1 * v2
    else:
        print("Unknown operation", operation)


def monkey_turn(monkeys, id):
    monkey = monkeys[id]
    items = monkey['items']
    monkey['items'] = []

    for item in items:
        worry = resolve(monkey['operation'], item) % globalMod
        monkey['inspected'] += 1
        if worry % monkey['test'] == 0:
            monkeys[monkey['true']]['items'].append(worry)
        else:
            monkeys[monkey['false']]['items'].append(worry)


def run1(lines):
    global globalMod
    monkeys = []
    rounds = 10000
    for i in range(0, len(lines), 7):
        monkeys.append(parse_monkey(lines[i:i+6]))


    globalMod = reduce(lambda a, b: a*b, [m['test'] for m in monkeys])
    print(globalMod)


    for i in range(rounds):
        for id in range(len(monkeys)):
            monkey_turn(monkeys, id)

    counts = sorted([monkey['inspected'] for monkey in monkeys], reverse=True)
    print(monkeys)
    return counts[0] * counts[1]


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = list(map(str.strip, f.readlines()))
        print(run1(lines))