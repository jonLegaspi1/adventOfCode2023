import sys
f = open(sys.argv[1]).read().strip()
ans = 0

for line in f.split('\n'):
    validGame = True
    id_, line = line.split(':')
    for event in line.split(';'):
        for balls in event.split(','):
            n, color = balls.split()
            if int(n) > {'red' : 12, 'green' : 13, 'blue' : 14}.get(color, 0):
                validGame = False
    if validGame:
        ans += int(id_.split()[-1])
print(ans)