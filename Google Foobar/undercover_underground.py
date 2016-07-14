import math
from math import factorial

# used for memoizing binomial coefficient calculation
mem_choose = {}

# used for memoizing total number of possible graphs for n, k
mem_graphs = {}

# used for memoizing recursive relation of counting distinct graphs
mem_counts = {}


def choose(n, k):
	comb = (n, k)
	if comb not in mem_counts:
		mem_choose[comb] = factorial(n) / (factorial(k) * factorial(n - k))
	return mem_choose[comb]


def possible_graphs(n, k):
	"""
    Returns the total number of graphs with that can be formed using
    n nodes and k vertices.
    """
	if (n, k) not in mem_graphs:
		mem_graphs[(n, k)] = choose(n * (n - 1) // 2, k)

	return mem_graphs[(n, k)]


def count(n, k):
	"""
    Returns the number of distinct, connected, labelled, undirected
    graphs that can be formed using 'n' nodes and 'k' vertices
    """
	if (n, k) in mem_counts:
		# memoized
		return mem_counts[(n, k)]

	if k == n - 1:
		# Cayley's formula
		c = int(n ** (n - 2))

	else:

		# number of possible vertices
		p = n * (n - 1) >> 1

		if k == p:
			# only way is to connect each node to all other nodes,
			# therefore only a single distinct graph
			c = 1

		else:

			# initially all possible graphs
			c = choose(p, k)

			# there can only be duplicates or unconnected components
			# if the number of nodes is less than p - n + 2.
			# equivalent of k < (n - 1 choose 2)
			if k < p - n + 2:

				for i in range(1, n):
					x = choose(n - 1, i - 1)

					# minimum of possible vertices for 'i' nodes and 'k'
					y = min(i * (i - 1) >> 1, k)

					for j in range(i - 1, y + 1):
						# exclude invalid graphs from the total
						c -= x * possible_graphs(n - i, k - j) * count(i, j)

	mem_counts[(n, k)] = c
	return c


def answer(n, k):
	return count(n, k)

#
