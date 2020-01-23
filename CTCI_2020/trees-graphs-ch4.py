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

	def find_stack(self, data):
		""" Return node object w/ this data 
		Iterative solution (but can be recursive)

		Uses a Stack - LIFO
		
		Depth First Search 
		"""

		# Start a STACK to keep track of nodes to visit.
		to_visit = [self]

		while to_visit:
			# Pop the last item on the list
			curr = to_visit.pop()

			if curr.data == data:
				return curr

			# Else, it is not them.
			# add children list to end of  'to visit' list
			to_visit.extend(curr.children) 

			# If they do not have children, they just get popped
			# and you go to the next one in the stack...

		def find_queue(self, data):
			""" Return node object w/ this data
			Simply by changing to queue

			we can do a FIFO

			Breadth First Search!! 
			"""

			# Goal : get a higher ranking node

			to_visit = [self] # QUEUE

			while to_visit:
				curr = to_visit.pop(0) # Get the highest (first in queue)

				if curr.data == data:
					return curr

				# Else, add all children to the queue
				to_visit.extend(curr.children)






# She said these make Things more complicated
class Tree:
	""" Class representing a Tree

		** EXPLAINATION **
		You know that a Node is itself a Tree??
		That means, it's a little 'extra' to make a Tree class at all.

		So, here we want to make sure a single node has all
		the functionality it needs. That is why Node defines
		a .find() method!

		And here, we wrote a find_in_tree method that literally
		just calls the Node.find() method cuz we want to 
		keep the sexy encapsulation.

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
	""" A Binary Search node for trees or graphs

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
	def __init__(self, data, left=None, right=None):
		# Doesnt take left and right because we must leave that to the 
		# 'insert' method - that takes care of the ordering of the 
		# new nodes when adding them to the tree.

		self.left = left
		self.right = right
		self.data = data

	def __repr__(self):
		"""Debugging-friendly representation."""

		return "<BinaryNode {data}>".format(data=self.data)


	def insert(self, data):
		# Suppose the parent is 'self ' - the root
		# We want to add one child - new node with data
		# * Recursively * 
		# Compare the value ' data ' of a new node with the 
			# parent node ' self.data ' 
			# and decides where to add it to the tree

		print('self.data', self.data)

		if self.data != None: 

			# Try the left side		
			if data < self.data:

				# If left branch is empty, add new node to left
				if self.left == None:
					print('self.left', self.left)
					self.left = BinaryNode(data)
					print('self.left', self.left)
				else:
					self.left.insert(data) # Recursive call

			elif data > self.data:
				if self.right == None:
					print('self.right', self.right)
					self.right = BinaryNode(data)
					print('self.right', self.right)
				else:
					print('recursive, both branches are full', self.left, self.right)
					self.right.insert(data)
		else:
			# If self.data == None, set self.data to new data
			# We are creating the head with the root?
			self.data = data



	def find(self, sought):
		""" Start at the node you're at ( where
		'self' is treated like a root, every time)

		Use a while loop 

		Go through, looking left and right. 

		Update curr in the 'right direction'

		Return node with this data. 
		Start at root and return None if not found
		"""
		# Start at the root
		curr = self

		while curr:

			print('checking curr.data', curr.data)

			if curr.data == sought:
				return curr

			elif sought < curr.data:
				curr = curr.left

			elif sought > curr.data:
				curr = curr.right

		return "None"




	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
			print(self.data)
		if self.right:
			self.right.PrintTree()

if __name__ == "__main__":

	apple = BinaryNode("apple")
	ghost = BinaryNode("ghost")
	fence = BinaryNode("fence", apple, ghost)
	just = BinaryNode('just')
	jackal = BinaryNode("jackal", fence, just)
	zebra = BinaryNode("zebra")
	pencil = BinaryNode("pencil", None, zebra)
	mystic = BinaryNode("mystic")
	pluto = BinaryNode("nerd", mystic, pencil)
	money = BinaryNode("money", jackal, pluto)

	print(money.find("nerd"))

	# root = BinaryNode(12)
	# print(root)

	# root.insert(3)
	# root.insert(2)
	# root.insert(10)
	# root.insert(11)


	# import doctest
	# doctest.testmod()

	# Make a filesystem
	# resume = Node("resume.txt", [])
	# recipes = Node("recipes.txt", [])
	# jane = Node("jane/", [resume, recipes])
	# server = Node("server.py", [])
	# jessica = Node("jessica/", [server])
	# users = Node("Users/", [jane, jessica])
	# root = Node("/", [users])

	# tree = Tree(root)
	# print("server.py = ", tree.find_in_tree("server.py")) # Will find
	# print("style.css = ", tree.find_in_tree("style.css")) # will not find


class Traversals:
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


# if __name__ == "__main__":
	# import doctest
	# doctest.testmod()

	# Make a filesystem
	# resume = Node("resume.txt", [])
	# recipes = Node("recipes.txt", [])
	# jane = Node("jane/", [resume, recipes])
	# server = Node("server.py", [])
	# jessica = Node("jessica/", [server])
	# users = Node("Users/", [jane, jessica])
	# root = Node("/", [users])

	# tree = Tree(root)
	# print("server.py = ", tree.find_in_tree("server.py")) # Will find
	# print("style.css = ", tree.find_in_tree("style.css")) # will not find

	# pass



















