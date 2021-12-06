def puzzle_1():
    depth = 0
    horizontal = 0
    with open('input.txt', 'r') as f:
        for line in f:
            command, amount = line.split(' ')
            if (command == 'forward'):
                horizontal += int(amount)
            elif (command == 'down'):
                depth += int(amount)
            elif (command == 'up'):
                depth -= int(amount)
    
    return depth * horizontal

def puzzle_2():
    depth = 0
    horizontal = 0
    aim = 0
    with open('input.txt', 'r') as f:
        for line in f:
            command, amount = line.split(' ')
            if (command == 'forward'):
                horizontal += int(amount)
                depth += aim * int(amount)
            elif (command == 'down'):
                aim += int(amount)
            elif (command == 'up'):
                aim -= int(amount)
    
    return depth * horizontal

print(puzzle_2())