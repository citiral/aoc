import sys

def is_integer(v):
    c = v[0]
    return ord(c) >= ord('0') and ord(c) <= ord('9')

def run1(inp):
    values =  {}
    pending_operations = [line.strip() for line in inp]

    while len(pending_operations) > 0:
        next_operations = []
        print(pending_operations)
        print(values)
        for instr in pending_operations:
            line = instr.strip()
            source, dest = line.split(" -> ")
            source = source.split()

            if len(source) == 1:
                if is_integer(source[0]):
                    values[dest] = int(source[0])
                elif source[0] in values:
                    values[dest] = values[source[0]]
                else:
                    next_operations.append(instr)
            elif len(source) == 2:
                if is_integer(source[1]):
                    values[dest] = ~int(source[1])
                elif source[1] in values:
                    values[dest] = ~values[source[1]]
                else:
                    next_operations.append(instr)
            elif len(source) == 3:
                if not is_integer(source[0]) and source[0] not in values:
                    next_operations.append(instr)
                elif not is_integer(source[2]) and source[2] not in values:
                    next_operations.append(instr)
                else:
                    if is_integer(source[0]):
                        v1 = int(source[0])
                    else:
                        v1 = values[source[0]]

                    if is_integer(source[2]):
                        v2 = int(source[2])
                    else:
                        v2 = values[source[2]]
                
                    if source[1] == 'AND':
                        values[dest] = v1 & v2
                    elif source[1] == 'OR':
                        values[dest] = v1 | v2
                    elif source[1] == 'LSHIFT':
                        values[dest] = v1 << v2
                    elif source[1] == 'RSHIFT':
                        values[dest] = v1 >> v2


        pending_operations = next_operations
    return values

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.readlines()
        print(run1(inp))