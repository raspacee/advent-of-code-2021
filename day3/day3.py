def puzzle_1():
    gamma = ''

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines[0])):
            count_0 = 0
            count_1 = 0
            for line in lines:
                if line[i] == '0':
                    count_0 += 1
                elif line[i] == '1':
                    count_1 += 1
            if (count_0 > count_1):
                gamma += '0'
            elif (count_1 > count_0):
                gamma += '1'
    
    epsilon = ['1' if c == '0' else '0' for c in gamma]
    epsilon = ''.join(epsilon)
    
    return int(gamma, 2) * int(epsilon, 2) 

def puzzle_2():
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        finder(lines, 0, True, '')
        finder(lines, 0, False, '')

def finder(lines, i, maximum_count, rating):
    if ((len(lines) == 1) or (len(lines) == 2 and lines[0] == lines[1])):
        print(int(lines[0], 2))
        return

    count_0 = 0
    count_1 = 0
    for line in lines:
        if line[i] == '0':
            count_0 += 1
        elif line[i] == '1':
            count_1 += 1
    if maximum_count:
        if (count_0 > count_1):
            lines = list(filter(lambda l: l[i] == '0', lines))
            rating += '0'
        else:
            lines = list(filter(lambda l: l[i] == '1', lines))
            rating += '1'
    else:
        if (count_1 < count_0):
            lines = list(filter(lambda l: l[i] == '1', lines))
            rating += '1'
        else:
            lines = list(filter(lambda l: l[i] == '0', lines))
            rating += '0'
    
    finder(lines, i + 1, maximum_count, rating)