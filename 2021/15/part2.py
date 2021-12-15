# thank you, wikipedia

with open('input.txt') as f:
	s = f.read().split()

smol_board = [[int(i) for i in row] for row in s]
n = len(smol_board)
m = len(smol_board[0])

def inc(k, x):
	x += k
	x %= 9
	return x + (x == 0) * 9

board = [[0 for i in range(5*m)] for j in range(5*n)]


for i in range(n):
	for j in range(m):
		for ii in range(5):
			for jj in range(5):
				board[i+ii*n][j+jj*m] = inc(ii+jj, smol_board[i][j])


n = len(board)
m = len(board[0])

def is_valid(p):
	i, j = p
	return (0 <= i < n) and (0 <= j < n)

def neighbors(p):
	i, j = p
	arr = [
	(i+1, j),
	(i-1, j),
	(i, j+1),
	(i, j-1)
	]

	return filter(is_valid, arr)

from queue import PriorityQueue

def dijkstra():
	q = PriorityQueue()

	dist = {}
	dist[(0, 0)] = 0

	for i in range(n):
		for j in range(m):
			v = (i, j)

			if v != (0, 0):
				dist[v] = float('inf')

			q.put((dist[v], v))

	while not q.empty():
		u = q.get()[1]

		for v in neighbors(u):
			i, j = v
			alt = dist[u] + board[i][j]

			if alt < dist[v]:
				dist[v] = alt
				q.put((alt, v))

	return dist


dist = dijkstra()

print(dist[(n-1, m-1)])