with open('input.txt') as f:
	s = f.read().splitlines()

numbers = [*map(int, s[0].split(','))]

boards = []
for i in range(1, len(s), 6):
	boards.append([[*map(int, s[i+1+k].split())] for k in range(5)])

n = len(boards)
seen = [ [[False]*5 for _ in range(5)] for _ in range(n) ]

def bingo_row(k, row):
	return all(seen[k][row])

def bingo_col(k, col):
	return all(seen[k][i][col] for i in range(len(seen[k])))

def bingo(k):
	if any(bingo_row(k, row) for row in range(len(seen[k]))):
		return True
	if any(bingo_col(k, col) for col in range(len(seen[k]))):
		return True
	return False

def update(k, number):
	board = boards[k]
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == number:
				seen[k][i][j] = True
				return

done = False
for number in numbers:
	for k in range(len(boards)):
		update(k, number)

		if bingo(k):
			board = boards[k]
			sum_ = 0
			for i in range(len(board)):
				for j in range(len(board[i])):
					if not seen[k][i][j]:
						sum_ += board[i][j]
			print(sum_ * number)
			done = True
			break

	if done:
		break
