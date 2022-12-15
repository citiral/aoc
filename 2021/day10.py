import sys

openers = "[({<"
closers = "])}>"
expected = {
    "[": "]",
    "{": "}",
    "<": ">",
    "(": ")",
}
fail_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
incomplete_scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

def parse_line(line):
    print("parsing line " + line)
    stack = []
    for c in line:
        if c in openers:
            stack.append(c)
        else:
            top = stack.pop()
            if c != expected[top]:
                return 0
    
    score = 0
    for v in stack[::-1]:
        score *= 5
        score += incomplete_scores[v]
    return score

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f.readlines()]

        scores = []
        for line in lines:
            s = parse_line(line)
            if s != 0:
                scores.append(s)
            
        scores = sorted(scores)
        print(scores)
        print(scores[int(len(scores) / 2)])