import sys

def run(lines):
    calories = [0]
    for line in lines:
        line = line.strip()
        if line == "":
            calories.append(0)
        else:
            calories[-1] += int(line)
    
    #print(sum(sorted(calories)[-3:]))
    print(sorted(calories))
    

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        run(lines)