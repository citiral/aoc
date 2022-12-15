import sys

def parse_coord(l):
    return [int(w) for w in l.split(",")]

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f.readlines()]
        
        field = {}

        for l in lines:
            start, end = [parse_coord(l) for l in l.split(" -> ")]
            
            if start[0] == end[0]:
                x = start[0]
                for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
                    if (x, y) in field:
                        field[(x, y)] += 1
                    else:
                        field[(x, y)] = 1
            
            elif start[1] == end[1]:
                y = start[1]
                for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
                    if (x, y) in field:
                        field[(x, y)] += 1
                    else:
                        field[(x, y)] = 1

            else:
                if start[0] < end[0]:
                    sx = 1
                else:
                    sx = -1
                if start[1] < end[1]:
                    sy = 1
                else:
                    sy = -1

                s = min(start[0], end[0])
                e = max(start[0], end[0])
                for i in range(e - s + 1):
                    pos = (start[0] + i*sx, start[1] + i*sy)
                    if pos in field:
                        field[pos] += 1
                    else:
                        field[pos] = 1        
        
        sum = sum([1 for v in field if field[v] > 1])

        print(sum)