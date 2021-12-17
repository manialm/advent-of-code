# 246403935575 too high
with open('input.txt') as f:
	s = f.read()

def hex_to_bin(string):
	return ''.join(bin(int(c, 16))[2:].zfill(4) for c in string)

s = hex_to_bin(s)
ans = 0

def evaluate(packet):
	version = packet[:3]
	typeid = int(packet[3:6], 2)

	packet = packet[6:]

	if typeid == 4:
		length, res = evaluate_literal(packet)
		return length + 6, res

	length, res = evaluate_operator(packet, typeid)
	return length + 6, res


def evaluate_literal(string):
	i = 0
	res = ''
	while string[i] != '0':
		res += string[i+1:i+5]
		i += 5

	res += string[i+1:i+5]
	i += 5

	return i, int(res, 2)


func = {
0: lambda x, y: x + y,
1: lambda x, y: x * y,
2: lambda x, y: min(x, y),
3: lambda x, y: max(x, y),
5: lambda x, y: int(x > y),
6: lambda x, y: int(x < y),
7: lambda x, y: int(x == y),
}

def evaluate_operator(string, typeid):
	length_typeid = string[0]

	accum = None
	f = func[typeid]

	if length_typeid == '0':
		num_bits = int(string[1:1+15], 2)
		curr = 1+15

		bits = 0
		while bits < num_bits:
			length, res = evaluate(string[curr:])

			if accum is not None:
				accum = f(accum, res)
			else:
				accum = res

			curr += length
			bits += length

	else:
		num_packets = int(string[1:1+11], 2)
		curr = 1+11

		for i in range(num_packets):
			length, res = evaluate(string[curr:])

			if accum is not None:
				accum = f(accum, res)
			else:
				accum = res
				
			curr += length

	return curr, accum

_, res = evaluate(s)
print(res)