from collections import Counter

with open('input.txt', 'r') as f:
    start, rules = f.read().strip().split('\n\n')
    R = {}
    for line in rules.strip().split('\n'):
        s,e = line.strip().split(' -> ')
        R[s] = e

def puzzle_both():
    global start, R
    
    table = Counter()
    for i in range(len(start) - 1):
        table[start[i] + start[i + 1]] += 1
    
    for step in range(41):
        if step == 10 or step == 40:
            L = Counter()
            for k in table:
                L[k[0]] += table[k]
            L[start[-1]] += 1
            print(max(L.values()) - min(L.values()))

        tmp = Counter()
        for k in table:
            tmp[k[0] + R[k]] += table[k]
            tmp[R[k] + k[1]] += table[k]
        table = tmp

puzzle_both()