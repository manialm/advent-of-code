with open('input.txt') as f:
    s = f.read().split(',')

s = [int(i) for i in s]
s.sort()

median = s[len(s)//2]
print(sum(abs(x-median) for x in s))