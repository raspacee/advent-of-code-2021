def puzzle_1():
    increased = 0

    with open('input.txt', 'r') as f:
        first = f.readline()
        for line in f:
            if int(line) > int(first):
                increased += 1
            first = int(line)
    return increased

def puzzle_2():
    line_counter = 0
    increased = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [int(line) for line in lines]

        while (line_counter < len(lines) - 3):
            if (lines[line_counter] + lines[line_counter + 1] + lines[line_counter + 2] 
                < lines[line_counter + 1] + lines[line_counter + 2] + lines[line_counter + 3]):
                increased += 1
            line_counter += 1
    return increased