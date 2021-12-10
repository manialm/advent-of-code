with open('input.txt') as f:
	s = f.read().splitlines()

open = '([{<'
def closes(a, b):
	close = ')]}>'
	return close.index(a) == open.index(b)

def corrupted(s):
	stack = []

	for c in s:
		if c in open:
			stack.append(c)
		else:
			if not closes(c, stack.pop()):
				return c

	return None

score = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
}

res = 0
for line in s:
	if (c := corrupted(line)):
		res += score[c]

print(res)