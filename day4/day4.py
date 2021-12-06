def puzzle_1():
    with open('input.txt', 'r') as f:
        bingo_numbers = f.readline().split(',')
        bingo_numbers = [int(n) for n in bingo_numbers]
        boards = []

        for line in f:
            if line == '\n':
                board = []
                for i in range(5):
                    row = list(filter(lambda r: r != '', f.readline().split(' ')))
                    row = [int(r) for r in row]
                    board.append(row)
                boards.append(board)
                
        for n in bingo_numbers:
            for board in boards:
                apply_bingo(board, n)
                if is_bingo(board):
                    print(f'Won by number {n}!\n')
                    unmarked_sum = 0
                    for row in board:
                        for col in row:
                            if col != -1:
                                unmarked_sum += col
                    
                    print(f'Score is {unmarked_sum * n}')
                    return

def puzzle_2():
    with open('input.txt', 'r') as f:
        bingo_numbers = f.readline().split(',')
        bingo_numbers = [int(n) for n in bingo_numbers]
        boards = []

        for line in f:
            if line == '\n':
                board = []
                for i in range(5):
                    row = list(filter(lambda r: r != '', f.readline().split(' ')))
                    row = [int(r) for r in row]
                    board.append(row)
                boards.append(board)
                
        for n in bingo_numbers:
            for board in boards:
                apply_bingo(board, n)
                if is_bingo(board):
                    if len(boards) == 1:
                        print(f'Won by number {n}!\n')
                        unmarked_sum = 0
                        for row in board:
                            for col in row:
                                if col != -1:
                                    unmarked_sum += col
                        
                        print(f'Score is {unmarked_sum * n}')
                        return
            
            for board in boards:
                if is_bingo(board):
                    boards.remove(board)

def apply_bingo(board, n):
    for ridx, row in enumerate(board):
        for cidx, col in enumerate(row):
            if col == n:
                board[ridx][cidx] = -1

def is_bingo(board):
    # check rows
    for ridx in range(5):
        r = list(filter(lambda n: n == -1, board[ridx]))
        if len(r) == 5:
            return True
    
    # check columns
    for cidx in range(5):
        count = 0
        for ridx in range(5):
            if board[ridx][cidx] == -1:
                count += 1
        if count == 5:
            return True
    
    return False