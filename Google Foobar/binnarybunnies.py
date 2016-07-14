from math import factorial


class BST:
	"""
	BST implementation that can be initialized using an array of unique values.
	Manages only insertion.
	"""
	def __init__(self, *values):
		self.root = None
		self.left = None
		self.right = None

		for v in values:
			self.insert(v)

	def insert(self,value):
		if not self.root:
			self.root = value
		elif value < self.root:
			if not self.left:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if not self.right:
				self.right = BST(value)
			else:
				self.right.insert(value)


def choose(n, k):
	"""
	Returns binomial coefficient for n,k
	"""
	return factorial(n) / (factorial(k) * factorial(n-k))


def nodes(root):
	"""
	Returns the number of nodes in the tree.
	"""
	if not root:
		return 0
	else:
		return 1 + nodes(root.left) + nodes(root.right)


def sequences(root):
	"""
	Determines the number of permutations of an array that can form a BST
	identical to the one given.
	"""
	if not root:
		return 1

	# Get number of nodes in each subtree
	left_nodes = nodes(root.left)
	right_nodes = nodes(root.right)

	# Recrusively compute permutations for each subtree
	left_permutations = sequences(root.left)
	right_permutations = sequences(root.right)

	# Return number of ways to choose nodes in a subtree using maximum no of nodes
	# Multiply with number of permutations of each subtree
	return choose(left_nodes + right_nodes, right_nodes) * left_permutations * right_permutations


def answer(seq):
    return sequences(BST(*seq))