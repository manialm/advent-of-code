steps = 40

with open('input.txt') as f:
	template, rules = f.read().split('\n\n')
	rules = dict(rule.split(' -> ') for rule in rules.split('\n'))

d = dict.fromkeys(rules.keys(), 0)

def update():
	global d

	new_d = dict(d)

	for k, v in d.items():
		if v >= 1:
			new_d[k] -= v
			new = rules[k]
			new_d[ k[0] + new ] += v
			new_d[ new  + k[1]] += v

	d = new_d

for i in range(len(template) - 1):
	s = template[i:i+2]
	d[s] += 1

for _ in range(steps):
	update()

letters = ''.join(d.keys())
counter = dict.fromkeys(letters, 0)

for k, v in d.items():
	for c in k:
		counter[c] += v

counter = {k: v // 2 for k, v in counter.items()}
counter[template[0]] += 1
counter[template[-1]] += 1

maxi = max(counter.values())
mini = min(counter.values())
print(maxi - mini)