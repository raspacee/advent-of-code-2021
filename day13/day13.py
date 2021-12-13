from pprint import pprint

cords = moves = []
with open('input.txt', 'r') as f:
    lines = f.read()
    cords, folds = lines.strip().split('\n\n')
    cords = [[int(c.split(',')[0]), int(c.split(',')[1])] for c in cords.split('\n')]
    folds = [{f.split('=')[0][-1]: int(f.split('=')[1])} for f in folds.split('\n')]

lr = lc = 0
for c in cords:
    lc = max(c[0], lc)
    lr = max(c[1], lr)

board = [['.' for i in range(lc + 1)] for j in range(lr + 1)]
for c in cords:
    board[c[1]][c[0]] = '#'

def puzzle():
    global board
    for f in folds:
        if folds[1] == f:
            get_score()
        fold(list(f.keys())[0], list(f.values())[0])
    for r in board:
        print('')
        for c in r:
            if c != '.':
                print('x', end='')
            else:
                print(' ', end='')
    print('\n')

def fold(p, v):
    global board
    if p == 'y':
        b1 = board[:v]
        b2 = board[v + 1:]
        b2.reverse()
        baord = combine(b1, b2)
        board = board[:v]
    elif p == 'x':
        b1 = [b[:v] for b in board] 
        b2 = [b[v + 1:] for b in board] 
        b2 = [b[::-1] for b in b2]
        board = combine(b1, b2)
        board = [b[:v] for b in board] 

def combine(b1, b2):
    for r in range(len(b1)):
        for c in range(len(b1[r])):
            if b2[r][c] == '#':
                b1[r][c] = '#'
    return b1

def get_score():
    score = 0
    for r in board:
        for c in r:
            if c == '#':
                score += 1
    print(score)

puzzle()