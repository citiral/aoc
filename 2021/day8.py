import sys

def decode(wires, output):
    wires_1 = [o for o in wires if len(o) == 2][0]
    wires_4 = [o for o in wires if len(o) == 4][0]
    wires_7 = [o for o in wires if len(o) == 3][0]
    wires_8 = [o for o in wires if len(o) == 7][0]

    # top => 7 - 1
    top = wires_7.difference(wires_1)
    
    # 9 - (7 + 4)
    wires_4_plus_7 = wires_4.union(wires_7)
    wires_9 = [o for o in wires if wires_4_plus_7.issubset(o) and len(o.difference(wires_4_plus_7)) == 1][0]
    
    bottom_left = wires_8.difference(wires_9)

    bottom = wires_8.difference(wires_4.union(wires_7).union(bottom_left))

    
    wires_7_bottom_bottomleft = wires_7.union(bottom).union(bottom_left)
    wires_0 = [o for o in wires if len(o) == 6 and wires_7_bottom_bottomleft.issubset(o) and len(o - wires_7_bottom_bottomleft) == 1][0]
    top_left = wires_0 - wires_7_bottom_bottomleft
    middle = wires_8 - wires_0

    wires_top_middle_bottom_bottomleft = top.union(middle).union(bottom).union(bottom_left)
    wires_2 = [o for o in wires if len(o) == 5 and wires_top_middle_bottom_bottomleft.issubset(o) and len(o - wires_top_middle_bottom_bottomleft) == 1][0]
    top_right = wires_2 - wires_top_middle_bottom_bottomleft

    bottom_right = wires_8 - top.union(middle).union(bottom).union(top_left).union(top_right).union(bottom_left)
    wires_3 = (wires_2 - bottom_left).union(bottom_right)
    wires_4 = middle.union(top_left).union(top_right).union(bottom_right)
    wires_6 = wires_8 - top_right
    wires_5 = wires_6 - bottom_left

    #print(0, wires_0)
    #print(1, wires_1)
    #print(2, wires_2)
    #print(3, wires_3)
    #print(4, wires_4)
    #print(5, wires_5)
    #print(6, wires_6)
    #print(7, wires_7)
    #print(8, wires_8)
    #print(9, wires_9)

    score = 0
    for v in output:
        score *= 10
        if v == wires_0:
            score += 0
        elif v == wires_1:
            score += 1
        elif v == wires_2:
            score += 2
        elif v == wires_3:
            score += 3
        elif v == wires_4:
            score += 4
        elif v == wires_5:
            score += 5
        elif v == wires_6:
            score += 6
        elif v == wires_7:
            score += 7
        elif v == wires_8:
            score += 8
        elif v == wires_9:
            score += 9
    return score

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        entries = f.readlines()

        count = 0

        for entry in entries:
            signals, output = [[set(v) for v in v.split()] for v in entry.split(" | ")]
            s = decode(signals, output)
            print(s)
            count += s
        
        print(count)