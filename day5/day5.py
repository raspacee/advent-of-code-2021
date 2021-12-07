def read_coordinates(filename):
    coords = []

    with open(filename, 'r') as f:
        for line in f:
            tmp = []
            for c in line.split(' -> '):
                points = c.split(',')
                points = tuple([int(p) for p in points])
                tmp.append(tuple(points))
            coords.append(tmp)
    return coords

def puzzle_1():
    positions = {}
    coords = read_coordinates('input.txt')

    for c in coords:
        min_value = 0
        max_value = 0

        if (c[0][0] != c[1][0] and c[0][1] != c[1][1]):
            continue
        elif c[0][0] == c[0][1] and c[1][0] == c[1][1]:
            continue
        elif c[0][0] == c[1][0]:
            min_value = min(c[0][1], c[1][1])
            max_value = max(c[0][1], c[1][1])
            
            for i in range(min_value, max_value + 1):
                p = (c[0][0], i)
                if positions.get(p) != None:
                    positions[p] += 1
                else:
                    positions[p] = 0
        elif c[0][1] == c[1][1]:
            min_value = min(c[0][0], c[1][0])
            max_value = max(c[0][0], c[1][0])
            
            for i in range(min_value, max_value + 1):
                p = (i, c[1][1])
                if positions.get(p) != None:
                    positions[p] += 1
                else:
                    positions[p] = 0

    overlaps = 0
    for p, o in positions.items():
        if o > 0:
            overlaps += 1
    print(overlaps)

def puzzle_2():
    positions = {}
    coords = read_coordinates('input.txt')

    for c in coords:
        min_value = 0
        max_value = 0

        if (c[0][0] != c[1][0] and c[0][1] != c[1][1]):
            x_list = []
            y_list = []
            if c[0][0] > c[1][0]:
                x = c[0][0]
                while (x >= c[1][0]):
                    x_list.append(x)
                    x -= 1
            elif c[0][0] < c[1][0]:
                x = c[0][0]
                while (x <= c[1][0]):
                    x_list.append(x)
                    x += 1
            if c[0][1] > c[1][1]:
                y = c[0][1]
                while (y >= c[1][1]):
                    y_list.append(y)
                    y -= 1
            elif c[0][1] < c[1][1]:
                y = c[0][1]
                while (y <= c[1][1]):
                    y_list.append(y)
                    y += 1

            for p in list(zip(x_list, y_list)):
                if positions.get(p) != None:
                    positions[p] += 1
                else:
                    positions[p] = 0
        elif c[0][0] == c[0][1] and c[1][0] == c[1][1]:
            for i in range(c[0][0], c[1][1] + 1):
                p = (i, i)
                if positions.get(p) != None:
                    positions[p] += 1
                else:
                    positions[p] = 0
        elif c[0][0] == c[1][0]:
            min_value = min(c[0][1], c[1][1])
            max_value = max(c[0][1], c[1][1])
            
            for i in range(min_value, max_value + 1):
                p = (c[0][0], i)
                if positions.get(p) != None:
                    positions[p] += 1
                else:
                    positions[p] = 0
        elif c[0][1] == c[1][1]:
            min_value = min(c[0][0], c[1][0])
            max_value = max(c[0][0], c[1][0])
            
            for i in range(min_value, max_value + 1):
                p = (i, c[1][1])
                if positions.get(p) != None:
                    positions[p] += 1
                else:
                    positions[p] = 0

    overlaps = 0
    for p, o in positions.items():
        if o > 0:
            overlaps += 1
    print(overlaps)

puzzle_1()
puzzle_2()
