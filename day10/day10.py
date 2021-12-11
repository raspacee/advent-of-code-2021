def puzzle_1():
    point_table = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    open_braces = '[{(<'

    score = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            chunk = []
            for c in line:
                if c in open_braces: 
                    chunk.append(c)
                elif (c == ']' and chunk[-1] != '[') or (c == '}' and chunk[-1] != '{') or (c == '>' and chunk[-1] != '<') or (c == ')' and chunk[-1] != '('):
                    score += point_table[c]
                    break
                else:
                    chunk.pop()
    print('Puzzle 1 score is', score)

def puzzle_2():
    open_braces = '[{(<'
    scores = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            chunk = []
            for i, c in enumerate(line):
                if c in open_braces:
                    chunk.append(c)
                elif (c == ']' and chunk[-1] != '[') or (c == '}' and chunk[-1] != '{') or (c == '>' and chunk[-1] != '<') or (c == ')' and chunk[-1] != '('):
                    break
                elif (len(line) - 1) == i and len(chunk) > 1:
                    completion = complete_chunk(chunk)
                    scores.append(get_score(completion))
                else:
                    chunk.pop()
    scores.sort()
    print('Puzzle 2 score is', scores[int(len(scores) / 2)])
    
def get_score(completion):
    point_table = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4 
    }
    score = 0
    for c in completion:
        score = (score * 5) + point_table[c]
    return score

def complete_chunk(chunk):
    braces = {
        '{': '}',
        '(': ')',
        '<': '>',
        '[': ']'
    }
    completion = []
    for i in range(len(chunk) - 1, -1, -1):
        completion.append(braces[chunk[i]]) 
    return completion
    
puzzle_1()
puzzle_2()