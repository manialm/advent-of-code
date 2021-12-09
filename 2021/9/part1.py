with open('input.txt') as f:
	s = f.read().split()

height = [[int(c) for c in x] for x in s]

n = len(height)
m = len(height[0])

def is_valid(p):
	x, y = p
	return (0 <= x <= n-1) and (0 <= y <= m-1)

def is_low(x, y):
	arr = [
	(x+1, y),
	(x-1, y),
	(x, y+1),
	(x, y-1)
	]

	low = True
	for xx, yy in filter(is_valid, arr):
		if not (height[x][y] < height[xx][yy]):
			low = False
			break

	return low

res = sum(is_low(x, y) and (height[x][y] + 1) or 0 for x in range(n) for y in range(m))
print(res)
