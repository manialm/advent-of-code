with open('input.txt') as f:
	s = f.read().split('\n')
	
res = 0
for line in s:
	_, line = line.split(' | ')
	res += sum(1 for i in line.split() if len(i) in [2, 3, 4, 7])

print(res)