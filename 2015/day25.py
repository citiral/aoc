import sys
import itertools


def next_val(v):
    return (v * 252533) % 33554393


def run1(input):
    s = input[0].strip().split()
    end_row = int(s[-3][:-1])
    end_col = int(s[-1][:-1])
    val = 20151125
    row, col = 1, 1

    mc = 0
    mr = 0
    
    while row != end_row or col != end_col:
        val = next_val(val)

        if row == 1:
            row = col+1
            col = 1
        else:
            row -= 1
            col += 1
        
        #if row > mr or col > mc:
        #    mc = max(mc, col)
        #    mr = max(mr, row)
        #    print(mc, mr)
    
    return val


if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))