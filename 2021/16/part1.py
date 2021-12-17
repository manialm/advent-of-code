with open('input.txt') as f:
	s = f.read()

def hex_to_bin(string):
	return ''.join(bin(int(c, 16))[2:].zfill(4) for c in string)

s = hex_to_bin(s)
ans = 0

def parse(packet):
	global ans

	if not packet:
		return 0

	version = packet[:3]
	typeid = packet[3:6]

	ans += int(version, 2)

	packet = packet[6:]
	if typeid == '100':
		return parse_literal(packet) + 6
	return parse_operator(packet) + 6


def parse_literal(string):
	i = 0
	res = ''
	while string[i] != '0':
		res += string[i+1:i+5]
		i += 5

	res += string[i+1:i+5]
	i += 5

	return i


def parse_operator(string):
	length_typeid = string[0]

	if length_typeid == '0':
		num_bits = int(string[1:1+15], 2)
		curr = 1+15

		bits = 0
		while bits < num_bits:
			length = parse(string[curr:])
			curr += length
			bits += length

	else:
		num_packets = int(string[1:1+11], 2)
		curr = 1+11

		for i in range(num_packets):
			curr += parse(string[curr:])

	return curr

parse(s)
print(ans)