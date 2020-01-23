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

"Min-Heap"
	- 

"""

class Node:
	""" A general node for trees or graphs
		>>> n3 = Node('n3')
		>>> print(n3)
		Leaf n3
		>>> n2 = Node('n2', [n3]), 
		>>> print(n2)
		(Node n2 [Leaf n3],)
		>>> n1 = Node('n1', children=[n2, Node('n4')])
		>>> print(n1)
		Node n1 [(Node n2 [Leaf n3],), Leaf n4]
	"""

	def __init__(self, data, children=[]):
		self.data = data
		self.children = children

	def __repr__(self):
		# return self.children
		if self.children == []:
			return 'Leaf ' + str(self.data)
		else:
			return 'Node ' + str(self.data) + ' ' + str(self.children)

	def find(self, data):
		""" Return node object w/ this data """

		# Start a list to keep track of nodes to visit.
		to_visit = [self]

		while to_visit:
			curr = to_visit.pop()

			if curr.data == data:
				return curr

			# Else, add all children to 'to visit' list
			to_visit.extend(curr.children)

# She said these make Things more complicated
class Tree:
	""" Class representing a Tree
		>>> tree_root = Node('tree_root', [...])
		>>> t = Tree(tree_root)
		>>> print(t)
		>>> t.find_in_tree(1)

	"""

	def __init__(self, root):
		self.root = root

	def __repr__(self):
		"""Reader-friendly representation."""
		return "<Tree root={root}>".format(root=self.root)

	def find_in_tree(self, data):
		"""Return node object with this data.

		Start at root.
		Use the method from root to find the data
		Return None if not found.
		"""
		return self.root.find(data)

	def list_nodes_recursive(self, node):
		print(node.data)
		for child in node.children:
			list_nodes_recursive(child)









class BinaryNode():
	""" A Binary node for trees or graphs

		# Create root node:
		>>> bn = BinaryNode(0)
		>>> print(bn.data, bn.right, bn.left)
		0 None None

		# Add a new data - creates a new node & decides if it should go right or left:
		>>> bl = BinaryNode(-1)
		>>> bn.insert(-1)
		>>> bn.PrintTree()
		0

	"""
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data


	def insert(self, data):
		# *Recursively * Compare the value ' data ' of a new node with the 
			# parent node ' self.data ' 
			# and decides where to add it to the tree

		# print('inserting', data, self.data)
		if self.data != None: 
			# print(self.data)

			# Try the left side		
			if data < self.data:

				# If left branch is empty, add new node to left
				if self.left == None:
					
					self.left = BinaryNode(data)
					# print(self.left.data)
				else:
					self.left.insert(data) # Recursive call

			elif data > self.data:
				if self.right == None:
					self.right = BinaryNode(data)
				else:
					self.right.insert(data)
		else:
			self.data = data


	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
			print(self.data)
		if self.right:
			self.right.PrintTree()

"""
Traversals:
	- In order traversal
			Visit the left branch, then current, then right
	- Pre-order traversal
			Visits the current node before its child nodes
	- Post-order traversal
			Visits the current node after its child nodes
"""
def in_order_traversal(treeNode):
	""" Takes a TreeNode and visits the current nodes before its 
		child nodes
	"""
	if treeNode != None:
		in_order_traversal(node.left)
		visit(node)
		in_order_traversal(node.right)

def pre_order_traversal(treeNode):
	""" Takes a TreeNode and visits the current nodes before its 
		child nodes
	"""
	if treeNode != None:
		visit(node)
		pre_order_traversal(node.left)
		pre_order_traversal(node.right)



def post_order_traversal(treeNode):
	""" Takes a TreeNode and visits the current nodes after its 
		child nodes

		The root will always be the last node visited.
	"""
	if treeNode != None:
		
		pre_order_traversal(node.left)
		post_order_traversal(node.right)
		visit(node)








if __name__ == "__main__":
	# import doctest
	# doctest.testmod()

	# Make a filesystem
	resume = Node("resume.txt", [])
	recipes = Node("recipes.txt", [])
	jane = Node("jane/", [resume, recipes])
	server = Node("server.py", [])
	jessica = Node("jessica/", [server])
	users = Node("Users/", [jane, jessica])
	root = Node("/", [users])

	tree = Tree(root)
	print("server.py = ", tree.find_in_tree("server.py")) # Will find
	print("style.css = ", tree.find_in_tree("style.css")) # will not find




















