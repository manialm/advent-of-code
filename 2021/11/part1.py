with open('input.txt') as f:
	s = f.read().split()

board = [[int(c) for c in x] for x in s]
n = len(board)
m = len(board[0])

def is_valid(p):
	i, j = p
	return (0 <= i <= n-1) and (0 <= j <= m-1)

def neighbors(i, j):
	arr = []

	for dx in [-1, 0, 1]:
		for dy in [-1, 0, 1]:
			if not (dx == 0 and dy == 0):
				arr.append((i+dx, j+dy))

	return filter(is_valid, arr)

vis = set()
flashcount = 0
def flash(i, j):
	global board, vis, flashcount

	flashcount += 1
	vis.add((i, j))
	
	for ii, jj in neighbors(i, j):
		if not (ii, jj) in vis:
			board[ii][jj] += 1

	for ii in range(n):
		for jj in range(m):
			if board[ii][jj] > 9 and not (ii, jj) in vis:
				flash(ii, jj)

	board[i][j] = 0


def step():
	global board, vis

	vis = set()

	for i in range(n):
		for j in range(m):
			board[i][j] += 1

	for i in range(n):
		for j in range(m):
			if board[i][j] > 9:
				flash(i, j)


for i in range(100):
	step()

print(flashcount)