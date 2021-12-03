with open('input.txt') as f:
	s = f.read().splitlines()

gamma = ''
n = len(s)

for j in range(len(s[0])):
	d = {'0': 0, '1': 0}
	for i in range(n):
		k = s[i][j]
		d[k] += 1

	gamma += str(max(d, key=lambda k: d[k]))

m = len(gamma)
gamma = int(gamma, 2)
epsilon = 2**m - 1 - gamma
print(gamma*epsilon)