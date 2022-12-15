import sys
import math
import numpy as np
from pyquaternion import Quaternion
from scanf import scanf

def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])


def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def length(a):
    return math.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])

def sq_distance(a, b, indexes):
    return math.pow(a[indexes[0]] - b[indexes[0]], 2) + math.pow(a[indexes[1]] - b[indexes[1]], 2) + math.pow(a[indexes[2]] - b[indexes[2]], 2)

def normalized(v):
    l = length(v)
    return (v[0] / l, v[1] / l, v[2] / l)

def quat_from_to(fr, to):
    fr = normalized(fr)
    to = normalized(to)
    a = cross(fr, to)
    w = math.sqrt(math.pow(length(fr), 2) * math.pow(length(to), 2)) + dot(fr, to)
    return Quaternion(w, a[0], a[1], a[2])

def round(a):
    r = int(a)
    if a - r > 0.5:
        return r + 1
    return r

def rotate(v, quat):
    r = quat.rotate(v)
    return (round(r[0]), round(r[1]), round(r[2]))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def parse_scanners(lines):
    scanners = []
    for l in lines:
        if l.startswith("---"):
            scanners.append([])
        elif len(l.strip()) > 0:
            x, y, z = l.strip().split(",")
            scanners[-1].append((int(x), int(y), int(z)))
    return scanners


def do_scanners_match(scan1, scan2):
    base_pivot = scan1[0]
    base_target = scan1[1]

    for scan_pivot in scan2:
        offset = sub(base_pivot, scan_pivot)
        print(scan_pivot)
        for scan_target in scan2:
            if scan_target == scan_pivot:
                continue

            scan_target_translated = add(scan_target, offset)
           # print(scan_target, scan_target_translated)
            quat = quat_from_to(scan_target_translated, base_target)
            #print(quat, scan_target, scan_target_translated, rotate(scan_target_translated, quat))
            matchcount = 0
            for v in scan2:
                if v == scan_pivot or v == scan_target:
                    continue
                r = rotate(add(v, offset), quat)
                print(v, add(v, offset), r)
                if r in scan1:
                    matchcount += 1
            if matchcount > 0:
                return True
    return False


def calc_center(scan):
    center = scan[0]
    for v in scan[1:]:
        center = add(v, center)
    return (center[0] / len(scan), center[1] / len(scan), center[2] / len(scan))


def flip(v, flips):
    mx = 1 if flips[0] else -1
    my = 1 if flips[1] else -1
    mz = 1 if flips[2] else -1
    return (v[0] * mx, v[1] * my, v[2] * mz)


def calc_dist(s1, s2, center, offset, flips, indexes):
    return sq_distance(s1, flip(add(sub(s2, center), offset), flips), indexes)


def scanner_difference(scan1, scan2, offset, flips, indexes):
    score = 0
    center1 = calc_center(scan1)
    center2 = calc_center(scan2)
    for s1 in scan1:
        s1_centered = sub(s1, center1)
        score += min([calc_dist(s1_centered, s2, center2, offset, flips, indexes) for s2 in scan2])
    return score

possible_indexes = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 1, 0), (2, 0, 1)]


def get_derivative(scan1, scan2, offset, flips, indexes):
    doffsetx = scanner_difference(scan1, scan2, add(offset, (1, 0, 0)), flips, indexes) - scanner_difference(scan1, scan2, sub(offset, (1, 0, 0)), flips, indexes)
    doffsety = scanner_difference(scan1, scan2, add(offset, (0, 1, 0)), flips, indexes) - scanner_difference(scan1, scan2, sub(offset, (0, 1, 0)), flips, indexes)
    doffsetz = scanner_difference(scan1, scan2, add(offset, (0, 0, 1)), flips, indexes) - scanner_difference(scan1, scan2, sub(offset, (0, 0, 1)), flips, indexes)

    normal = scanner_difference(scan1, scan2, offset, flips, indexes)
    dflipx = 1 if scanner_difference(scan1, scan2, offset, (not flips[0], flips[1], flips[2]), indexes) < normal else 0
    dflipy = 1 if scanner_difference(scan1, scan2, offset, (flips[0], not flips[1], flips[2]), indexes) < normal else 0
    dflipz = 1 if scanner_difference(scan1, scan2, offset, (flips[0], flips[1], not flips[2]), indexes) < normal else 0
    
    best_index = indexes
    best_index_v = normal
    for possible_index in possible_indexes:
        dif = scanner_difference(scan1, scan2, offset, flips, possible_index) 
        if dif < normal:
            best_index = possible_index
            best_index_v = dif
    return normalized((doffsetx, doffsety, doffsetz)), (dflipx, dflipy, dflipz), (best_index)


def match_scanners(scan1, scan2):
    offset = [0, 0, 0]
    flips = [False, False, False]
    indexes = (0, 1, 2)

    for i in range(100):
        doffset, dflips, dindexes = get_derivative(scan1, scan2, offset, flips, indexes)
        indexes = dindexes
        for i in range(3):
            if dflips[i]:
                flips[i] = not flips[i]
            offset[i] -= doffset[i] * 0.1
    
    diff = scanner_difference(scan1, scan2, offset, flips, indexes)
    print(diff)
    return True, offset, flips, indexes


def run1(lines):
    scanners = parse_scanners(lines)
    return match_scanners(scanners[1], scanners[2])#], (0, 0, 0), (False, False, False), (0, 1, 2))
    
    #return do_scanners_match(scanners[0], scanners[1])

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        print(run1(lines))