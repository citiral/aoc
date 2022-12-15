import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        heights = [int(line) for line in lines]

        count = 0
        for i in range(3, len(heights)):
            if heights[i - 3] + heights[i - 2] + heights[i - 1] < heights[i] + heights[i - 2] + heights[i - 1]:
                count += 1
    
    print(count)