import sys
import itertools

def run1(input,):
    molecule = "HOH"
    found = set()
    
    for line in input:
        values = line.strip().split()
        inp, outp = values[0], values[2]
        offset = 0
        while True:
            f = molecule.find(inp, offset)
            if f == -1:
                break
            l = len(inp)
            result = molecule[:f] + outp + molecule[f+l:]
            offset += l
            found.add(result)
    return len(found)


def calc_count(input, target):
    found = set([target])
    step = 0
    while not "E" in found:
        nextfound = set()
        for molecule in found:
            for values in input:
                outp, inp = values[0], values[2]
                offset = 0
                while True:
                    f = molecule.find(inp, offset)
                    if f == -1:
                        break
                    l = len(inp)
                    result = molecule[:f] + outp + molecule[f+l:]
                    offset += l
                    nextfound.add(result)
        found = nextfound
        step += 1
        print(step, len(found))
    return step


def run2(input):
    finaltarget = "C(12(B2(F)6BP66BF)PB1252(6BPBP3)12(63)12512(F)(2(F)66BF)112(25112(3)F,2(F,1F)25125PBP63)1P(24)PB112(F,251(F))112(PB2(F)3,1111251124)112(PB24)B1111251PB25PBPB12(F,F)2512(F)B112(F,F)251PB2512(P3)(F)P6B1P(F)11112(112(F,F)F)B125F)5252(6(P3)F)1251PB12(BF)11P(11P3)2(F,F)125(PBP3)"

    count = len(finaltarget) -  finaltarget.count('(') -  finaltarget.count(')') - 2*finaltarget.count(',') - 1
    return count
        


if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = [l.strip().split() for l in f.readlines()]
        print(run2(inp))