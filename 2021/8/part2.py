from itertools import permutations

with open('input.txt') as f:
	s = f.read().split('\n')

nums = [''.join(sorted(s)) for s in 'abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg'.split()]
good = sorted(nums)
index = {s: nums.index(s) for s in good}

res = 0
for line in s:
	patterns, digits = line.split(' | ')
	patterns = patterns.split()
	digits = digits.split()

	for p in permutations('abcdefg'):
		table = str.maketrans('abcdefg', ''.join(p))

		arr = []
		for pattern in patterns:
			pattern = pattern.translate(table)
			pattern = ''.join(sorted(pattern))
			arr.append(pattern)

		arr.sort()
		if arr == good:
			num = ''
			for digit in digits:
				digit = digit.translate(table)
				digit = ''.join(sorted(digit))
				num += str(index[digit])
			res += int(num)
			break

print(res)