from collections import defaultdict

adj = defaultdict(lambda: [])

with open('input.txt') as f:
	for line in f:
		u, v = line.strip().split('-')
		adj[u] += [v]
		adj[v] += [u]


vis = []
count = 0
twice = ''
def dfs(v):
	global count, twice
	
	if v in vis:
		twice = v

	if v[0].islower():
		vis.append(v)

	if v == 'end':
		count += 1
		vis.pop()
		return

	for u in adj[v]:
		if u not in vis or (not twice and u != 'start'):
			dfs(u)

	if v[0].islower():
		vis.pop()

	if v in vis:
		twice = ''


dfs('start')
print(count)