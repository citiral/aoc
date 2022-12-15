import sys


def run1(lines):
    empty = set()
    beacons = set()
    sensors = set()
    checkrow = 10

    for line in lines:
        values = line.strip().split()
        sensor_x = int(values[2][2:-1])
        sensor_y = int(values[3][2:-1])
        beacon_x = int(values[-2][2:-1])
        beacon_y = int(values[-1][2:])

        dx = abs(beacon_x - sensor_x)
        dy = abs(beacon_y - sensor_y)
        dist = dx + dy
        print(line, dist)

        sensors.add((sensor_x, sensor_y))
        beacons.add((beacon_x, beacon_y))

        if checkrow <= sensor_y - dist and checkrow >= sensor_y + dist:
            continue
        

        for x in range(sensor_x - dist, sensor_x + dist + 1):
            y = checkrow
            if abs(x-sensor_x) + abs(y-sensor_y) > dx + dy:
                continue
            empty.add((x, y))

    result = 0
    for pos in empty:
        x, y = pos
        if y == checkrow and pos not in beacons:
            result += 1
    return result 



def split_span(spans, a_start, a_end):
    newspawns = []
    for span in spans:
        b_start, b_end = span
        if b_start >= a_start and b_end <= a_end:
            continue
        elif b_start < a_start and b_end > a_end:
            newspawns.append((b_start, a_start-1))
            newspawns.append((a_end+1, b_end))
        elif b_start < a_start and b_end < a_start:
            newspawns.append((b_start, b_end))
        elif b_start > a_end and b_end > a_end:
            newspawns.append((b_start, b_end))
        elif b_start < a_start:
            newspawns.append((b_start, a_start-1))
        else:
            newspawns.append((a_end+1, b_end))

    return newspawns


def run2(input):
    box_start = 0
    box_end = 4000000
    spans = [[(0, box_end)] for y in range(box_end+1)]

    for line in lines:
        print(line)
        values = line.strip().split()
        sensor_x = int(values[2][2:-1])
        sensor_y = int(values[3][2:-1])
        beacon_x = int(values[-2][2:-1])
        beacon_y = int(values[-1][2:])

        dx = abs(beacon_x - sensor_x)
        dy = abs(beacon_y - sensor_y)
        dist = dx + dy

        for y in range(-dist, dist+1):
            if y + sensor_y < 0 or y + sensor_y > box_end:
                continue

            start_x = sensor_x - (dist - abs(y))
            end_x = sensor_x + (dist - abs(y))

            spans[y+sensor_y] = split_span(spans[y + sensor_y], start_x, end_x)

    for y in range(box_end+1):
        s = spans[y]
        if len(s) > 1:
            print("error, should only be one")
        elif len(s) == 0:
            continue
        else:
            x = s[0][1]
            return x * 4000000 + y


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        print(run2(lines))