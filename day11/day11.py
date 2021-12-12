flashed = 0
octopuses = []

def puzzle_1():
    global flashed
    global octopuses

    with open('input.txt', 'r') as f:
        flashed = 0
        octopuses = []
        lines = f.readlines()
        for row in lines:
            tmp = []
            for col in row.strip('\n'):
                tmp.append(int(col))
            octopuses.append(tmp) 

    step = 0
    while (step < 100):
        for ridx, row in enumerate(octopuses):
            for cidx, col in enumerate(row):
                octopuses[ridx][cidx] += 1

        for ridx, row in enumerate(octopuses):
            for cidx, col in enumerate(row):
                if octopuses[ridx][cidx] > 9:
                    flash(ridx, cidx)
        
        for ridx, row in enumerate(octopuses):
            for cidx, col in enumerate(row):
                if octopuses[ridx][cidx] == -1:
                    octopuses[ridx][cidx] = 0
        step += 1
    print('Puzzle 1:', flashed)

def puzzle_2():
    global flashed
    global octopuses

    with open('input.txt', 'r') as f:
        flashed = 0
        octopuses = []
        lines = f.readlines()
        for row in lines:
            tmp = []
            for col in row.strip('\n'):
                tmp.append(int(col))
            octopuses.append(tmp) 

    step = 0
    while step >= 0:
        step += 1
        for ridx, row in enumerate(octopuses):
            for cidx, col in enumerate(row):
                octopuses[ridx][cidx] += 1

        for ridx, row in enumerate(octopuses):
            for cidx, col in enumerate(row):
                if octopuses[ridx][cidx] > 9:
                    flash(ridx, cidx)
        
        all_flashed = True
        for ridx, row in enumerate(octopuses):
            for cidx, col in enumerate(row):
                if octopuses[ridx][cidx] == -1:
                    octopuses[ridx][cidx] = 0
                else:
                    all_flashed = False
        if all_flashed:
            print('Puzzle 2:', step)
            break

def flash(ridx, cidx):
    global flashed
    global octopuses
    flashed += 1
    octopuses[ridx][cidx] = -1

    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            rr = ridx + r;
            cc = cidx + c;
            if rr > -1 and rr < len(octopuses[0]) and cc > -1 and cc < len(octopuses) and octopuses[rr][cc] != -1:
                octopuses[rr][cc] += 1
                if octopuses[rr][cc] > 9:
                    flash(rr, cc)
    
puzzle_1()
puzzle_2()