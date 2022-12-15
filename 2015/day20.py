import sys
import itertools


def run1(input):
    input = int(input[0].strip())
    house = 0
    highest = 0
    while True:
        house += 1
        count = 0
        for i in range(1, house+1):
            if house % i == 0:
                count += i * 10
        if count > highest:
            print(count)
            highest = count
        if count >= input:
            return house
    

if __name__ == "__main__":
    with open(sys.argv[0][:-3] + ".txt", "r") as f:
        inp = f.readlines()
        print(run1(inp))