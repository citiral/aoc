import sys
import itertools


lost_fight = 99999999
bestspent = lost_fight

def best_fight(p0, p1, currentplayer, currentspent):
    global bestspent
    if currentspent >= bestspent:
        return lost_fight

    p0 = p0.copy()
    p1 = p1.copy()

    if p0['health'] <= 0:
        return lost_fight
    elif p1['health'] <= 0:
        bestspent = min(bestspent, currentspent)
        return 0
    
    if currentplayer == 0:
        p0['health'] -= 1
        if p0['health'] <= 0:
            return lost_fight
    
    if p0['shield'] > 0:
        p0['shield'] -= 1
    if p0['poison'] > 0:
        p0['poison'] -= 1
        p1['health'] -= 3
    if p0['recharge'] > 0:
        p0['recharge'] -= 1
        p0['mana'] += 101

    if p0['health'] <= 0:
        return lost_fight
    elif p1['health'] <= 0:
        bestspent = min(bestspent, currentspent)
        return 0

    if currentplayer == 0:
        bestoption = lost_fight
        if p0['mana'] >= 53:
            t_p0 = p0.copy()
            t_p1 = p1.copy()
            t_p0['mana'] -= 53
            t_p1['health'] -= 4
            bestoption = min(bestoption, best_fight(t_p0, t_p1, 1 - currentplayer, currentspent + 53) + 53)
        if p0['mana'] >= 73:
            t_p0 = p0.copy()
            t_p1 = p1.copy()
            t_p0['mana'] -= 73
            t_p0['health'] += 2
            t_p1['health'] -= 2
            bestoption = min(bestoption, best_fight(t_p0, t_p1, 1 - currentplayer, currentspent + 73) + 73)
        if p0['mana'] >= 113 and p0['shield'] == 0:
            t_p0 = p0.copy()
            t_p0['mana'] -= 113
            t_p0['shield'] = 6
            bestoption = min(bestoption, best_fight(t_p0, p1, 1 - currentplayer, currentspent + 113) + 113)
        if p0['mana'] >= 173 and p0['poison'] == 0:
            t_p0 = p0.copy()
            t_p0['mana'] -= 173
            t_p0['poison'] = 6
            bestoption = min(bestoption, best_fight(t_p0, p1, 1 - currentplayer, currentspent + 173) + 173)
        if p0['mana'] >= 229 and p0['recharge'] == 0:
            t_p0 = p0.copy()
            t_p0['mana'] -= 229
            t_p0['recharge'] = 5
            bestoption = min(bestoption, best_fight(t_p0, p1, 1 - currentplayer, currentspent + 229) + 229)
        return bestoption
    else:
        p0['health'] -= max(1, p1['damage'] - (7 if p0['shield'] > 0 else 0))
        return best_fight(p0, p1,  1 - currentplayer, currentspent)


def run1(input):
    player = {'health': 50, 'mana': 500, 'shield': 0, 'poison': 0, 'recharge': 0}
    boss = {'health': 55, 'damage': 8}

    return best_fight(player, boss, 0, 0)


if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))