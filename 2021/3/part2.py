import bisect

with open('input.txt') as f:
	s = f.read().splitlines()


s.sort()
olds = s.copy()

j = 0
while len(s) > 1:
	n = len(s)
	i = bisect.bisect_left([x[j] for x in s], '1')

	if i <= n // 2:
		s = s[i:]
	else:
		s = s[:i]

	j += 1

oxygen = s[0]


s = olds.copy()

j = 0
while len(s) > 1:
	n = len(s)
	i = bisect.bisect_left([x[j] for x in s], '1')

	if i > n // 2:
		s = s[i:]
	else:
		s = s[:i]

	j += 1

co2 = s[0]


oxygen = int(oxygen, 2)
co2 = int(co2, 2)
print(oxygen * co2)