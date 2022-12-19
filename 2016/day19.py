import sys

class Elf:
    id = 0
    presents = 1
    next = None
    prev = None


def run1(inp):
    count = int(inp[0].strip())
    first = None
    last = None

    for i in range(count):
        e = Elf()
        e.id = i+1
        e.presents = 1
        if first == None:
            first = e
        if last != None:
            last.next = e
        e.prev = last        
        last = e
    first.prev = last
    last.next = first

    cur = first
    while cur.next != cur:
        #print(f"elf {cur.id} takes elf {cur.next.id}'s presents")
        cur.presents += cur.next.presents
        cur.next = cur.next.next
        cur.next.prev = cur
        cur = cur.next
    return cur.id


def run2(inp):
    elves = [(i+1, 1) for i in range(int(inp[0].strip()))]
    i = 0

    while len(elves) != 1:
        target = (i + int(len(elves)/2)) % len(elves)
        if i % 10000 == 0:
            print(f"elf {elves[i][0]} takes elf {elves[target][0]}'s presents")
        elves[i] = (elves[i][0], elves[i][1] + elves[target][1])
        elves.pop(target)
        if i >= len(elves):
            i = 0
        elif target > i:
            i = (i + 1) % len(elves)
    
    return elves[0]
    
def run2a(inp):
    count = int(inp[0].strip())
    first = None
    last = None

    for i in range(count):
        e = Elf()
        e.id = i+1
        e.presents = 1
        if first == None:
            first = e
        if last != None:
            last.next = e
        e.prev = last        
        last = e
    first.prev = last
    last.next = first

    cur = first    
    skip = int(count / 2)
    target = cur
    while skip > 0:
        target = target.next
        skip -= 1

    while cur.next != cur:
        #print(f"elf {cur.id} takes elf {target.id}'s presents")
        cur.presents += target.presents

        target.prev.next = target.next
        target.next.prev = target.prev
        count -= 1
        cur = cur.next
        if count % 2 == 0:
            target = target.next.next
        else:
            target = target.next
    return cur.id

if __name__=="__main__":
    with open(sys.argv[0][:-2] + "txt", "r") as f:
        inp = f.readlines()
        print(run2a(inp))