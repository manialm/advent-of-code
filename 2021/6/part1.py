with open('input6.txt') as f:
    s = f.read().split(',')

arr = [int(i) for i in s]

def f(x):
    return 6 if x == 0 else x-1

def update(arr):
    return [f(x) for x in arr] + [8]*arr.count(0)
    
for _ in range(80):
    arr = update(arr)
    
print(len(arr))