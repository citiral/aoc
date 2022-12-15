import sys

def parse_coord(l):
    return [int(w) for w in l.split(",")]

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        positions = [int(f) for f in [l.strip() for l in f.readlines()][0].split(",")]
        print(positions)

        s = 0
        costs = []
        for i in range(1, max(positions) + 2):
            costs.append(s)
            s += i
        print(costs)

        best = None
        bestavg = None
        for i in range(len(positions)):
            avg = sum([costs[abs(p - i)] for p in positions])
            print(f"{i}: {avg}")

            if bestavg == None or avg < bestavg:
                best = i
                bestavg = avg
        
        print(f"best: {best} -> {bestavg}")