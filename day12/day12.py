from collections import defaultdict

G = defaultdict(list)

with open('input.txt', 'r') as f:
    for l in f.readlines():
        c1, c2 = l.strip().split('-')
        G[c1].append(c2)
        G[c2].append(c1)

def puzzle_1(p, visited):
    if p == 'end':
        return 1
    if p.islower() and p in visited:
        return 0
    visited = visited | { p }
    count = 0
    for n in G[p]:
        count += puzzle_1(n, visited)
    return count

def puzzle_2(p, visited, dup):
    if p == 'end':
        return 1
    if p == 'start' and visited:
        return 0
    if p.islower() and p in visited:
        if dup is None:
            dup = p
        else:
            return 0
    visited = visited | { p }
    count = 0
    for n in G[p]:
        count += puzzle_2(n, visited, dup)
    return count

print(puzzle_1('start', set()))
print(puzzle_2('start', set(), None))