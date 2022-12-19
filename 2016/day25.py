import sys
import itertools
import copy
import tqdm

def is_reg(v):
    return len(v) == 1 and ord(v) >= ord('a') and ord(v) <= ord('d')


def parse_reg(v):
    return ord(v) - ord('a')


def run_instruction(cpu, instr, inp):
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
    elif instr[0] == "out":
        a = instr[1]
        v = cpu['regs'][parse_reg(a)] if is_reg(a) else int(a)
        print(v, end ='', flush=True)
        if v != cpu['expected_out']:
            cpu['failed'] = True
        cpu['expected_out'] = 1 - cpu['expected_out']
        cpu['pc'] += 1
    else:
        print("Unknown instruction", instr)


def run1(instructions):


    i = 0
    while True:
        print(f'testing {i}')
        cpu = {'regs': [i, 0, 0, 0], 'pc': 0, 'expected_out': 0, 'failed': False}
        while cpu['pc'] >= 0 and cpu['pc'] < len(instructions) and not cpu['failed']:
            instr = instructions[cpu['pc']]
            run_instruction(cpu, instr, instructions)
        i += 1


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = [l.strip().split() for l in f.readlines()]
        print(run1(inp))