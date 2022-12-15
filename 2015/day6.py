import sys

def parse_coords(line):
    a = line.split(" ")[-3:]
    begin = list(map(int, a[0].split(",")))
    end = list(map(int, a[2].split(",")))

    return begin, end

def run1(inp):
    lights = {}
    for instruction in inp:
        begin, end = parse_coords(instruction)

        if instruction.startswith("turn on"):
            for i in range(begin[0], end[0]+1):
                for j in range(begin[1], end[1]+1):
                    coord = (i, j)
                    if coord in lights:
                        lights[(i, j)] += 1
                    else:
                        lights[(i, j)] = 1
        elif instruction.startswith("turn off"):
            for i in range(begin[0], end[0]+1):
                for j in range(begin[1], end[1]+1):
                    coord = (i, j)
                    if coord in lights:
                        lights[(i, j)] = max(0, lights[(i, j)] - 1)
                    else:
                        lights[(i, j)] = 0
        else:
            for i in range(begin[0], end[0]+1):
                for j in range(begin[1], end[1]+1):
                    coord = (i, j)
                    if coord in lights:
                        lights[coord] += 2
                    else:
                        lights[coord] = 2
    
    count = 0
    for l in lights:
        count += lights[l]
    return count
        
        


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.readlines()
        print(run1(inp))