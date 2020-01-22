""" Ch 4: Trees and Graphs ~~~~~~~~~~~~~~~~~~~~

* Note that Worst and avg case times may vary
* Ask lots of clarifying questions! 
* There are many types!

Graphs:
	- 

Trees
	- are a type of graph
	- composed of nodes
	- has a root node
	- each node has 0 or more child nodes
	- and so on, recursively

Binary Trees
	- A tree where each node has 0-2 children
	- 'leaf' is a node w/o children

Binary Search Tree
	- A Binary tree is a binary serach tree if
	all left descendenc <= n < all right descendents.
	- True for each node n
	- Clarify where duplicate values should be

"Balanced"
	- Not perfect, but more or less so
	- Approx O(log n) for `insert` and `find`

"Complete"
	- If you filled it from left to right, as you should,
	- The right slot is missing, not the left slot

"Full Binary Tree"
	- Each node has zero or two children
	- No nodes have only one child

"Perfect Binary Tree"
	- Both full and complete
	- All leaf nodes at same level
	- If so, a perfect tree has 2^k - 1 nodes


"""

class Node:
	""" A general node for trees or graphs
		>>> n3 = Node('n3')
		>>> print(n3)

		>>> n2 = Node('n2', [n3]), 
		>>> print(n2)

		>>>
		# Node n2[]
		# >>> n1 = Node('n1', children=[n2, n3])
		# >>> print(n1)
		# Node n1[]
	"""

	def __init__(self, data, children=[]):
		self.data = data
		self.children = children # left, right, ...

	def __repr__(self):
		# return self.children
		if self.children == []:
			return 'Leaf ' + self.data
		else:
			return 'Node ' + self.data + ', children: ' + str(self.children)


class BinaryNode(Node):
	""" A Binary node for trees or graphs
		# >>> bn = BinaryNode('bnode')
		# >>> print(bn)
		# Node bnode[]
		# >>> bn.insert('test')
		# >>> print(bn)
	"""

	# def insert(self, data):
	# 	# Compare the new value with the parent node
	# 	if self.data:

	# 		# Try the left side
	# 		if self.data < self.data:

	# 			# If left branch is empty, add new node to left
	# 			if self.left == None:
	# 				self.left = Node(data)


		







# She said these make Things more complicated

class Tree:
	""" Class representing a Tree
		tree_root = Node('tree_root', [...])
		t = Tree(tree_root)
	"""

	def __init__(self, root):
		self.root = root

class BinaryTree:
	""" Class representing a Binary Tree
		tree_root = Node('tree_root', [...])
		t = Tree(tree_root)
	"""

	def __init__(self, root):
		self.root = root


	def in_order_traversal(self, node):
		pass



if __name__ == "__main__":
	import doctest
	doctest.testmod()






















