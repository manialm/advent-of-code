with open('input.txt') as f:
	template, rules = f.read().split('\n\n')
	rules = dict(rule.split(' -> ') for rule in rules.split('\n'))

def update(s):
	res = s[0]
	for i in range(len(s)-1):
		x = s[i:i+2]
		res += rules[x] + x[1]

	return res

for _ in range(40):
	template = update(template)

from collections import Counter

counter = Counter(template)
print(max(counter.values()) - min(counter.values()))