import sys
import itertools


def run_combat(p1, p2):
    p1turn = True
    while p1['health'] > 0 and p2['health'] > 0:
        if p1turn:
            p2['health'] -= max(1, p1['damage'] - p2['armor'])
        else:
            p1['health'] -= max(1, p2['damage'] - p1['armor'])
        p1turn = not p1turn
    return p2['health'] <= 0


def make_player(health, damage, armor):
    return {'health': health, 'damage': damage, 'armor': armor}


def add_items(p, weapon, armor, ring1, ring2):
    return {
        'health': p['health'],
        'damage': p['damage'] + weapon[1] + armor[1] + ring1[1] + ring2[1],
        'armor': p['armor'] + weapon[2] + armor[2] + ring1[2] + ring2[2],
    }


def calc_cost(weapon, armor, ring1, ring2):
    return weapon[0] + armor[0] + ring1[0] + ring2[0]


def run1(input):
    weapons = {
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0)
    }
    armors = {
        (0, 0, 0),
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5),
    }
    rings = {
        (0, 0, 0),
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    }

    p1 = make_player(100, 0, 0)

    best = None

    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring1 == ring2:
                        continue
                    
                    p1_t = add_items(p1, weapon, armor, ring1, ring2)
                    if not run_combat(p1_t, make_player(103, 9, 2)):
                        cost = calc_cost(weapon, armor, ring1, ring2)
                        if best == None or best < cost:
                            best = cost
    return best


if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))