import sys

def increase_energy(field, x, y):
    if field[y][x] < 10:
        field[y][x] += 1
        if field[y][x] >= 10:
            flash_count = 1
            for ix in range(-1, 2):
                for iy in range(-1, 2):
                    if x + ix >= 0 and x + ix < len(field[0]) and y + iy >= 0 and y + iy < len(field):
                        flash_count += increase_energy(field, x + ix, y + iy)
            return flash_count
    return 0


def run_step(field):
    flash_count = 0
    for y in range(len(field)):
        for x in range(len(field[y])):
            flash_count += increase_energy(field, x, y)

    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == 10:
                field[y][x] = 0

    return flash_count

            
if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        field = [[int(c) for c in l.strip()] for l in f.readlines()]
        print(field)

        expected_flash_count = len(field) * len(field[0])
        i = 0
        while True:
            i += 1
            flash_count = run_step(field)
            if flash_count == expected_flash_count:
                print(f"{i}: {flash_count} flashes")
                break
