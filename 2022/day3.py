import sys
from enum import Enum


def get_score(item):
    item = ord(item)
    if item >= ord('a') and item <= ord('z'):
        return item - ord('a') + 1
    else:
        return item - ord('A') + 27

def run1(lines):
    score = 0
    for line in lines:
        line = line.strip()
        p1 = line[:int(len(line)/2)]
        p2 = line[int(len(line)/2):]
        
        for item in p1:
            if item in p2:
                score += get_score(item)
                break
    print(score)
    
def run2(lines):
    score = 0
    for i in range(0, len(lines), 3):
        line1 = lines[i].strip()
        line2 = lines[i+1].strip()
        line3 = lines[i+2].strip()
        
        for item in line1:
            if item in line2 and item in line3:
                score += get_score(item)
                break
    print(score)
    

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        run2(lines)