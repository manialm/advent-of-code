with open('input.txt') as f:
	points, folds = f.read().split('\n\n')
	points = [[*map(int, line.split(','))][::-1] for line in points.split()]
	folds = folds.split('\n')

n = max(p[0] for p in points) + 1
m = max(p[1] for p in points) + 1

board = [['.' for i in range(m)] for j in range(n)]

for p in points:
	x, y = p
	board[x][y] = '#'

def foldX(x):
	global board
	n = len(board)
	m = len(board[0])
	for xx in range(x+1, n):
		dx = xx - x
		new_x = x - dx
		for yy in range(m):
			if board[xx][yy] == '#':
				board[new_x][yy] = '#'

	board = board[:x]


def foldY(y):
	global board
	n = len(board)
	m = len(board[0])
	for yy in range(y+1, m):
		dy = yy - y
		new_y = y - dy
		for xx in range(n):
			if board[xx][yy] == '#':
				board[xx][new_y] = '#'

	board = [row[:y] for row in board]

for fold in folds:
	dir, val = fold.split()[-1].split('=')
	val = int(val)

	if dir == 'x':
		foldY(val)
	elif dir == 'y':
		foldX(val)

print(*[''.join(row) for row in board], sep='\n')