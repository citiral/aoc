import sys

def calc_basin(vents, basins, x, y, basin):

    v = vents[y][x]
    if v == 9:
        return 0
    else:
        score = 1
        basins[y][x] = basin
        
        if x > 0 and vents[y][x-1] > v and basins[y][x-1] == -1:
            score += calc_basin(vents, basins, x-1, y, basin)
        if x < width - 1 and vents[y][x+1] > v and basins[y][x+1] == -1:
            score += calc_basin(vents, basins, x+1, y, basin)
        if y > 0 and vents[y-1][x] > v and basins[y-1][x] == -1:
            score += calc_basin(vents, basins, x, y-1, basin)
        if y < height - 1 and vents[y+1][x] > v and basins[y+1][x] == -1:
            score += calc_basin(vents, basins, x, y+1, basin)
        
        return score


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        vents = [[int(c) for c in l.strip()] for l in f.readlines()]
        
        width = len(vents[0])
        height = len(vents)

        basins = [[-1 for i in range(width)] for j in range(height)]
        print(vents)
        score = 0

        basin_count = 0
        basin_scores = {}
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
                    if basins[y][x] == -1:
                        basin_scores[basin_count] = calc_basin(vents, basins, x, y, basin_count)
                        basin_count += 1
        
        print(basins)
        print(basin_scores)
        
        sorted_scores = sorted(list(basin_scores.values()), reverse=True)
        print(sorted_scores[0]*sorted_scores[1]*sorted_scores[2])