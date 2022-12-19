import sys


def process_rule(password, rule):
    v = [c for c in password]
    parts = rule.split()

    if rule.startswith("swap position"):
        a = int(parts[2])
        b = int(parts[5])
        c = password[a]
        v[a] = v[b]
        v[b] = c
    elif rule.startswith("swap letter"):
        a = parts[2]
        b = parts[5]
        ia = password.find(a)
        ib = password.find(b)
        c = v[ia]
        v[ia] = v[ib]
        v[ib] = c
    elif rule.startswith("reverse"):
        a = int(parts[2])
        b = int(parts[4])
        return password[0:a] + password[a:b+1][::-1] + password[b+1:]
    elif rule.startswith("rotate left"):
        steps = int(parts[2])
        return password[steps:] + password[0:steps]
    elif rule.startswith("rotate right"):
        steps = int(parts[2])
        return password[-steps:] + password[0:-steps]
    elif rule.startswith("rotate based"):
        steps = password.find(parts[6])
        if steps >= 4:
            steps += 2
        else:
            steps += 1
        steps = steps % len(password)
        return password[-steps:] + password[0:-steps]
    elif rule.startswith("move"):
        a = int(parts[2])
        b = int(parts[5])
        c = password[a]

        password = password[:a] + password[a+1:]
        return password[:b] + c + password[b:]

    return "".join(v)

def unprocess_rule(password, rule):
    v = [c for c in password]
    parts = rule.split()

    if rule.startswith("swap position"):
        a = int(parts[2])
        b = int(parts[5])
        c = password[a]
        v[a] = v[b]
        v[b] = c
    elif rule.startswith("swap letter"):
        a = parts[2]
        b = parts[5]
        ia = password.find(a)
        ib = password.find(b)
        c = v[ia]
        v[ia] = v[ib]
        v[ib] = c
    elif rule.startswith("reverse"):
        a = int(parts[2])
        b = int(parts[4])
        return password[0:a] + password[a:b+1][::-1] + password[b+1:]
    elif rule.startswith("rotate left"):
        steps = int(parts[2])
        return password[-steps:] + password[0:-steps]
    elif rule.startswith("rotate right"):
        steps = int(parts[2])
        return password[steps:] + password[0:steps]
    elif rule.startswith("rotate based"):
        result = password.find(parts[6])
        "01234567"
        steps = [1, 1, 6, 2, 7, 3, 0, 4][result]
        return password[steps:] + password[0:steps]
    elif rule.startswith("move"):
        b = int(parts[2])
        a = int(parts[5])
        c = password[a]

        password = password[:a] + password[a+1:]
        return password[:b] + c + password[b:]

    return "".join(v)
    

def run1(inp):
    password = "abcdefgh"

    for line in inp:
        line = line.strip()
        res = process_rule(password, line)
        undone = unprocess_rule(res, line)
        print(f"{line}: {password} -> {res} -> {undone}")
        if undone != password:
            return "ERR"
        password = res
        

    return password
    

def run2(inp):
    password = "fbgdceah"

    for line in inp[::-1]:
        line = line.strip()
        password = unprocess_rule(password, line)        

    return password


if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = f.readlines()
        print(run2(inp))