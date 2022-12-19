import sys
import hashlib


def has_repeat(v, x):
    for i in range(len(v) - x + 1):
        found = True
        for j in range(1, x):
            if v[i] != v[i+j]:
                found = False
                break
        if found:
            return True, v[i]
    return False, None

def repeats_c(v, x, c):
    for i in range(len(v) - x + 1):
        found = True
        for j in range(x):
            if c != v[i+j]:
                found = False
                break
        if found:
            return True
    return False


def stretched_hash(v):
    for i in range(2017):
        v = hashlib.md5(v.encode()).hexdigest()
    return v


def run1(inp):
    hashes = []
    keys_found = 0
    index = 0

    for i in range(1001):
        hashes.append(hashlib.md5(f"{inp}{i}".encode()).hexdigest())

    while keys_found != 64:
        repeats, c = has_repeat(hashes[index%1001], 3)
        if repeats:
            found = False
            for i in range(1, 1001):
                if repeats_c(hashes[(index+i)%1001], 5, c):
                    found = True
                    break
            if found:
                keys_found += 1
                print(f"key {keys_found} is {hashes[index%1001]} at index {index}")
        hashes[index%1001] = hashlib.md5(f"{inp}{index+1001}".encode()).hexdigest()
        index += 1

def run2(inp):
    hashes = []
    keys_found = 0
    index = 0

    for i in range(1001):
        hashes.append(stretched_hash(f"{inp}{i}"))

    while keys_found != 64:
        repeats, c = has_repeat(hashes[index%1001], 3)
        if repeats:
            found = False
            for i in range(1, 1001):
                if repeats_c(hashes[(index+i)%1001], 5, c):
                    found = True
                    break
            if found:
                keys_found += 1
                print(f"key {keys_found} is {hashes[index%1001]} at index {index}")
        hashes[index%1001] = stretched_hash(f"{inp}{index+1001}")
        index += 1


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = "zpqevtbw"
        print(run2(inp))