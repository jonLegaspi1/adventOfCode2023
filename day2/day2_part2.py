import sys
from collections import defaultdict
f = open(sys.argv[1]).read().strip()
ans = 0

for line in f.split('\n'):
    id_, line = line.split(':')
    minGame = defaultdict(int)
    for event in line.split(';'):
        for balls in event.split(','):
            n, color = balls.split()
            n = int(n)
            minGame[color] = max(minGame[color], n)
    temp = 1
    for val in minGame.values():
        temp *= val
    ans += temp            
print(ans)