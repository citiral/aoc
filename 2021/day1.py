import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        heights = [int(line) for line in lines]

        count = 0
        for i in range(1, len(heights)):
            if heights[i - 1] < heights[i]:
                count += 1
    
    print(count)