import sys

def fold_y(field, line):
    print(f"Folding y {line}")

    field_copy = field.copy()

    for (x, y) in field_copy:
        if y > line:
            del field[(x, y)]
            field[(x, line - (y - line))] = "#"

def fold_x(field, line):
    print(f"Folding x {line}")

    field_copy = field.copy()

    for (x, y) in field_copy:
        if x > line:
            del field[(x, y)]
            field[(line - (x - line)), y] = "#"

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        input = [l.strip() for l in f.readlines()]

        field = {}

        parsing_dots = True
        for line in input:
            if line == "":
                parsing_dots = False
                continue
            
            if parsing_dots:
                (x, y) = line.split(",")
                field[(int(x), int(y))] = '#'
            else:
                fold_amount = int(line.split("=")[1])
                if line.startswith("fold along y"):
                    fold_y(field, fold_amount)
                else:
                    fold_x(field, fold_amount)
                print(field)
        
        size_x = 0
        size_y = 0
        for (x, y) in field:
            size_x = max(size_x, x)
            size_y = max(size_y, y)

        for y in range(size_y+1):
            for x in range(size_x+1):
                if (x, y) in field:
                    print("#", end="")
                else:
                    print(" ", end="")
            print("")