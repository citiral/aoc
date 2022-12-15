import sys
import hashlib


def run1(inp):
    prefix = inp[0].strip()

    i = 0
    while True:
        data = inp + str(i)
        hash = hashlib.md5(data.encode()).hexdigest()
        if hash[0:6] == "000000":
            return i
        i += 1


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.readlines()
        print(run1(inp[0]))