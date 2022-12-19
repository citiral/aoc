import sys
import itertools
import copy


def is_reg(v):
    return len(v) == 1 and ord(v) >= ord('a') and ord(v) <= ord('d')


def parse_reg(v):
    return ord(v) - ord('a')


heatmap = []

def run_instruction(cpu, instr, inp):
    heatmap[cpu["pc"]] += 1
    if cpu["pc"] == 19:
        print(cpu)
        cpu["regs"][0] = 479001600
    if instr[0] == "cpy":
        a = instr[1]
        b = instr[2]

        if is_reg(b):
            cpu['regs'][parse_reg(b)] = cpu['regs'][parse_reg(a)] if is_reg(a) else int(a)
        cpu['pc'] += 1
    elif instr[0] == "inc":
        a = instr[1]
        if is_reg(a):
            cpu['regs'][parse_reg(a)] += 1
        cpu['pc'] += 1
    elif instr[0] == "dec":
        a = instr[1]
        if is_reg(a):
            cpu['regs'][parse_reg(a)] -= 1
        cpu['pc'] += 1
    elif instr[0] == "jnz":
        a = instr[1]
        b = instr[2]
        v = cpu['regs'][parse_reg(a)] if is_reg(a) else int(a)
        if v == 0:
            cpu['pc'] += 1
        else:
            cpu['pc'] += cpu['regs'][parse_reg(b)] if is_reg(b) else int(b)
    elif instr[0] == "tgl":
        a = instr[1]
        offset = cpu['pc'] + cpu['regs'][parse_reg(a)] if is_reg(a) else int(a)

        if offset < len(inp):
            old_instr = inp[offset]
            if len(old_instr) == 2:
                if old_instr[0] == "inc":
                    inp[offset][0] = "dec"
                else:
                    inp[offset][0] = "inc"
            else:
                if old_instr[0] == "jnz":
                    inp[offset][0] = "cpy"
                else:
                    inp[offset][0] = "jnz"

        cpu['pc'] += 1

    else:
        print("Unknown instruction", instr)

def run1(inp):
    global heatmap
    for i in range(6, 9):
        heatmap = [0 for i in range(len(inp))]
        cpu = {'regs': [i, 0, 0, 0], 'pc': 0}

        instructions = copy.deepcopy(inp)
        while cpu['pc'] >= 0 and cpu['pc'] < len(instructions):
            instr = instructions[cpu['pc']]
            run_instruction(cpu, instr, instructions)
        print(f"{i} {cpu}")

        #print("##################")
        #for i in range(len(inp)):
        #    print(" ".join(inp[i]) + f" #{heatmap[i]}")


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = [l.strip().split() for l in f.readlines()]
        print(run1(inp))