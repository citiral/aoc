import sys
import itertools
import copy


def is_reg(v):
    return len(v) == 1 and ord(v) >= ord('a') and ord(v) <= ord('d')


def parse_reg(v):
    return ord(v) - ord('a')


def run_instruction(cpu, instr):
    if instr[0] == "cpy":
        a = instr[1]
        b = instr[2]

        cpu['regs'][parse_reg(b)] = cpu['regs'][parse_reg(a)] if is_reg(a) else int(a)
        cpu['pc'] += 1
    elif instr[0] == "inc":
        a = instr[1]
        cpu['regs'][parse_reg(a)] += 1
        cpu['pc'] += 1
    elif instr[0] == "dec":
        a = instr[1]
        cpu['regs'][parse_reg(a)] -= 1
        cpu['pc'] += 1
    elif instr[0] == "jnz":
        a = instr[1]
        v = cpu['regs'][parse_reg(a)] if is_reg(a) else int(a)
        if v == 0:
            cpu['pc'] += 1
        else:
            cpu['pc'] += int(instr[2])
    else:
        print("Unknown instruction", instr)

def run1(inp):
    cpu = {'regs': [0, 0, 1, 0], 'pc': 0}

    while cpu['pc'] >= 0 and cpu['pc'] < len(inp):
        instr = inp[cpu['pc']]
        run_instruction(cpu, instr)
    
    return cpu


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = [l.strip().split() for l in f.readlines()]
        print(run1(inp))