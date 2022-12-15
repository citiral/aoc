import sys

def parse_coord(l):
    return [int(w) for w in l.split(",")]

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        fish_inputs = [int(f) for f in [l.strip() for l in f.readlines()][0].split(",")]
        fish_counts = [0] * 9

        for fish in fish_inputs:
            fish_counts[fish] += 1


        for i in range(67856*67856):
            new_fish_counts = [0] * 9
            
            new_fish_counts[0] = fish_counts[1]
            new_fish_counts[1] = fish_counts[2]
            new_fish_counts[2] = fish_counts[3]
            new_fish_counts[3] = fish_counts[4]
            new_fish_counts[4] = fish_counts[5]
            new_fish_counts[5] = fish_counts[6]
            new_fish_counts[6] = fish_counts[7] + fish_counts[0]
            new_fish_counts[7] = fish_counts[8]
            new_fish_counts[8] = fish_counts[0]
            
            fish_counts = new_fish_counts
        
        print(fish_counts)
        print(sum(fish_counts))