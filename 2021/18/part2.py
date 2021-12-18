class Node:
	def __init__(self, value=None, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

	def modify(self, node):
		parent = self.parent

		if self.parent.left is self:
			self.parent.left = node
		elif self.parent.right is self:
			self.parent.right = node

		node.parent = parent

	def set_left(self, left):
		self.left = left
		self.left.parent = self

	def set_right(self, right):
		self.right = right
		self.right.parent = self

	def is_leaf(self):
		return (self.left is None) and (self.right is None)

	def is_pair(self):
		return (not self.is_leaf()) and self.left.is_leaf() and self.right.is_leaf()

	def subtree_first(self):
		while self.left is not None:
			self = self.left
		return self

	def subtree_last(self):
		while self.right is not None:
			self = self.right
		return self

	def successor(self):
		if self.right:
			return self.right.subtree_first()

		while self.parent and (self is self.parent.right):
			self = self.parent

		return self.parent

	def predecessor(self):
		if self.left:
			return self.left.subtree_last()

		while self.parent and (self is self.parent.left):
			self = self.parent

		return self.parent


	def __iter__(self):
		return iter( (self.left, self.right) )

	def __add__(self, other):
		node = Node()
		node.set_left(self)
		node.set_right(other)
		return node

	def __repr__(self):
		if self.is_leaf():
			return repr(self.value)
		return f'[{self.left},{self.right}]'


def parse(s):
	if '[' not in s:
		return Node(value=int(s))

	left_done = False
	left, right = '', ''

	depth = 0
	for i, c in enumerate(s[1:-1]):
		depth += (c == '[')
		depth -= (c == ']')

		if depth == 0 and c == ',':
			continue

		if not left_done:
			left += c
		else:
			right += c

		if depth == 0:
			left_done = True

	node = Node()
	node.set_left(parse(left))
	node.set_right(parse(right))

	return node


def explode(pair):
	left, right = pair

	succ = right.successor()
	if succ:
		succ = succ.right.subtree_first()
		succ.modify( Node(succ.value + right.value) )

	pred = left.predecessor()
	if pred:
		pred = pred.left.subtree_last()
		pred.modify( Node(pred.value + left.value) )

	pair.modify(Node(0))


def split(node):
	a = node.value // 2
	b = node.value - a

	new = Node()
	new.set_left( Node(a) )
	new.set_right( Node(b) )
	node.modify(new)


def reduce_explode(node, depth=0):
	if depth >= 4 and node.is_pair():
		explode(node)
		return True

	if node.left:
		if reduce_explode(node.left, depth+1):
			return True

	if node.right:
		if reduce_explode(node.right, depth+1):
			return True

	return False


def reduce_split(node):
	if node.is_leaf() and node.value >= 10:
		split(node)
		return True

	if node.left:
		if reduce_split(node.left):
			return True
	
	if node.right:
		if reduce_split(node.right):
			return True

	return False


def reduce(node):
	if not reduce_explode(node):
		if not reduce_split(node):
			return
	reduce(node)


def magnitude(node):
	if node.is_leaf():
		return node.value

	return 3 * magnitude(node.left) + 2 * magnitude(node.right)


with open('input.txt') as f:
	arr = f.read().split()

ans = 0
for x in arr:
	for y in arr:
		if x == y:
			continue

		node_x = parse(x)
		node_y = parse(y)

		node = node_x + node_y
		reduce(node)
		ans = max(ans, magnitude(node))

print(ans)