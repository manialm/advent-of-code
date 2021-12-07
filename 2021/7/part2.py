with open('input.txt') as f:
    s = f.read().split(',')

s = [int(i) for i in s]
s.sort()

mean = round(sum(s) / len(s))
median = s[len(s)//2]
a, b = sorted([mean, median])

f = lambda n: n*(n+1)//2
g = lambda x: sum(f(abs(i-x)) for i in s)
print(min(g(x) for x in range(a, b+1)))