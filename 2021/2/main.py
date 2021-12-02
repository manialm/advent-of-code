with open('input.txt') as f:
	s = f.readlines()

hor, ver = 0, 0
aim = 0
for line in s:
	dir, x = line.split()
	x = int(x)

	match dir:
		case "forward":
			hor += x
			ver += aim * x
		case "down":
			aim += x
		case "up":
			aim -= x

print(hor * aim)
print(hor * ver)