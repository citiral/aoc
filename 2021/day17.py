import sys
import math
from scanf import scanf

def calc_xmin(x):
    i = 0
    xmin = 0
    while i < x:
        i += xmin
        xmin += 1
    return xmin - 1

def get_target_duration(x, target):
    p = 0
    start = 0
    end = 0
    while x > 0:
        p += x
        x -= 1

        if p < target[0]:
            start += 1
            end += 1
        elif p <= target[1]:
            end += 1
        else:
            if start == end:
                return -1, -1
            return start+1, end
    return start+1, 999


def get_best_y_for_duration(dur, target):
    min_y = math.ceil(target[3] / dur)
    max_y = 300#math.floor(abs(target[2]) * dur)

    best_height = 0
    for y in range(min_y, max_y):
        max_height = 0
        y_pos = 0
        y_vel = y
        for i in range(dur):
            y_pos += y_vel
            max_height = max(y_pos, max_height)
            y_vel -= 1
            if y_pos >= target[2] and y_pos <= target[3]:
                best_height = max(max_height, best_height)
                print(y, best_height)
                break
    return best_height
        


def run1(lines):
    line = lines [0]
    target = scanf("target area: x=%d..%d, y=%d..%d", s = line)

    xmin = calc_xmin(target[0])
    xmax = target[1]

    longest_duration = 0
    for x in range(xmin, xmax+1):
        duration = get_target_duration(x, target)
        if (duration[0] == -1 and duration[1] == -1):
            continue
        print(duration)
        longest_duration = max(duration[1], longest_duration)
    
    print(get_best_y_for_duration(longest_duration, target))


valid_durs_cache = {}
def get_valid_y_durations(dur, target):
    global valid_durs_cache
    min_y = target[2]
    max_y = 300

    if dur in valid_durs_cache:
        return valid_durs_cache[dur]

    valid_durs = []
    for y in range(min_y, max_y):
        y_pos = 0
        y_vel = y
        for i in range(dur):
            y_pos += y_vel
            y_vel -= 1
        if y_pos >= target[2] and y_pos <= target[3]:
            valid_durs.append(y)
    valid_durs_cache[dur] = valid_durs
    return valid_durs


def run2(lines):
    line = lines [0]
    target = scanf("target area: x=%d..%d, y=%d..%d", s = line)

    xmin = calc_xmin(target[0])
    xmax = target[1]

    valid_durs = 0
    for x in range(xmin, xmax+1):
        x_durs = set()
        duration = get_target_duration(x, target)
        if (duration[0] == -1 and duration[1] == -1):
            continue
        
        for d in range(duration[0], duration[1]+1):
            y_vals = get_valid_y_durations(d, target)
            for y in y_vals:
                x_durs.add(y)
        valid_durs += len(x_durs)
        for d in x_durs:
            print(x, d)
    print(valid_durs)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f.readlines()]
        run2(lines)