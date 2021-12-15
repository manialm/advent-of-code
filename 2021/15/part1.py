with open('input.txt') as f:
	s = f.read().split()

board = [[int(i) for i in row] for row in s]
n = len(board)
m = len(board[0])

dp = [[0 for i in range(m)] for j in range(n)]
dp[0][0] = board[0][0]

for i in range(1, n):
	dp[i][0] = dp[i-1][0] + board[i][0]

for j in range(1, m):
	dp[0][j] = dp[0][j-1] + board[0][j]


for i in range(1, n):
	for j in range(1, m):
		dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + board[i][j]

print(dp[n-1][m-1] - dp[0][0])

