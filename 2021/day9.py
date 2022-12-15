import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        vents = [[int(c) for c in l.strip()] for l in f.readlines()]
        
        width = len(vents[0])
        height = len(vents)

        score = 0

        for x in range(width):
            for y in range(height):
                v = vents[y][x]

                if x > 0 and vents[y][x-1] <= v:
                    continue
                elif x < width - 1 and vents[y][x+1] <= v:
                    continue
                elif y > 0 and vents[y-1][x] <= v:
                    continue
                elif y < height - 1 and vents[y+1][x] <= v:
                    continue
                else:
                    score += v + 1
        
        print(score)