with open('input.txt') as f:
    s = f.read().splitlines()
    
def mrange(a, b):
    a, b = sorted((a, b))
    return range(a, b+1)

seen = {}
def update(x, y):
    global seen
    k = (x, y)
    seen[k] = seen.get(k, 0) + 1

for line in s:
    a, b = line.split(' -> ')
    x1, y1 = map(int, a.split(','))
    x2, y2 = map(int, b.split(','))

    if x1 == x2:
        for y in mrange(y1, y2+1):
            update(x1, y)
    elif y1 == y2:
        for x in mrange(x1, x2+1):
            update(x, y1)
    else:
        c = (x1 < x2) ^ (y1 < y2)
        if not c:
            for x, y in zip(mrange(x1, x2), mrange(y1, y2)):
                update(x, y)
        else:
            for x, y in zip(mrange(x1, x2), reversed(mrange(y1, y2))):
                update(x, y)
                    
        
res = len([k for k, v in seen.items() if v >= 2])
print(res)
            
    