from os import remove
import sys

def parse_board(lines):
    board = []
    for i in range(1, 6):
        board.append([int(w) for w in lines[i].split()])
    return board

def remove_number(board, n):
    for row in range(5):
        for col in range(5):
            if board[row][col] == n:
                board[row][col] = '.'

def sum_board(board):
    sum = 0
    for row in range(5):
        for col in range(5):
            if board[row][col] != '.':
                sum += board[row][col]
    return sum

def has_won(board):
    for row in range(5):
        won = True
        for col in range(5):
            if board[row][col] != '.':
                won = False
                break
        if won:
            return True

    for col in range(5):
        won = True
        for row in range(5):
            if board[row][col] != '.':
                won = False
                break
        if won:
            return True

    #won = True
    #for x in range(5):
    #    if board[x][x] != '.':
    #        won = False
    #        break
    #if won:
    #    return True
#
    #won = True
    #for x in range(5):
    #    if board[4-x][x] != '.':
    #        won = False
    #        break
    #if won:
    #    return True
    return False

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f.readlines()]
        
        draw = [int(l) for l in lines[0].split(",")]

        boards = []

        lines = lines[1:]
        while (len(lines) > 0):
            boards.append(parse_board(lines))
            lines = lines[6:]
        
        for d in draw:
            for b in boards:
                remove_number(b, d)

            for b in boards:
                if has_won(b):
                    if len(boards) == 1:
                        score = sum_board(b)
                        print(f"score: {score}, draw: {d}, mul: {score*d}")
                        print(b)
                        exit(0)
                    else:
                        boards.remove(b)