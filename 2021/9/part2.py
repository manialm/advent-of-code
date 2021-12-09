with open('input.txt') as f:
	s = f.read().split()

height = [[int(c) for c in x] for x in s]

n = len(height)
m = len(height[0])

def is_valid(p):
	x, y = p
	return (0 <= x <= n-1) and (0 <= y <= m-1)

def neighbors(x, y):
	arr = [
	(x+1, y),
	(x-1, y),
	(x, y+1),
	(x, y-1)
	]

	return filter(is_valid, arr)

def is_low(p):
	x, y = p
	
	low = True
	for xx, yy in neighbors(x, y):
		if not (height[x][y] < height[xx][yy]):
			low = False
			break

	return low

vis = set()
def dfs(p):
	x, y = p

	res = 0
	for u in neighbors(x, y):
		xx, yy = u

		if height[xx][yy] == 9:
			continue

		if u not in vis and height[xx][yy] > height[x][y]:
			vis.add(u)
			res += dfs(u)

	return 1 + res




lows = filter(is_low, ((x, y) for x in range(n) for y in range(m)))
basins = [dfs(v) for v in lows]

import heapq
x, y, z = heapq.nlargest(3, basins)

print(x * y * z)
