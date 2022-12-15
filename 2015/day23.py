import sys


def reg_index(a):
    if a == 'a':
        return 0
    if a == 'b':
        return 1
    else:
        print("unknown reg", a)


def run1(input):
    pc = {'regs': [1, 0], 'pc': 0}

    while pc['pc'] >= 0 and pc['pc'] < len(input):
        instr = input[pc['pc']]
        opp = instr[:3]

        if opp == "hlf":
            r = reg_index(instr[4:])
            pc['regs'][r] = int(pc['regs'][r]/2)
            pc['pc'] += 1
        elif opp == "tpl":
            r = reg_index(instr[4:])
            pc['regs'][r] = pc['regs'][r]*3
            pc['pc'] += 1
        elif opp == "inc":
            r = reg_index(instr[4:])
            pc['regs'][r] += 1
            pc['pc'] += 1
        elif opp == "jmp":
            offset = int(instr[4:])
            pc['pc'] += offset
        elif opp == "jie":
            offset = int(instr[7:])
            r = reg_index(instr[4])
            if pc['regs'][r] % 2 == 0:
                pc['pc'] += offset
            else:
                pc['pc'] += 1
        elif opp == "jio":
            offset = int(instr[7:])
            r = reg_index(instr[4])
            if pc['regs'][r] == 1:
                pc['pc'] += offset
            else:
                pc['pc'] += 1
        else:
            print("Unknown instruction", opp)
    return pc


if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = [l.strip() for l in f.readlines()]
        print(run1(inp))