with open('input.txt') as f:
	s = f.readlines()

s = [int(i) for i in s]

a = sum(s[i+1]>s[i] for i in range(len(s)-1))
b = sum(s[i+3]>s[i] for i in range(len(s)-3))
print(a, b)