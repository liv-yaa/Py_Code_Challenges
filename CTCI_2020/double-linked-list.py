# Singly Linked List Node

class LLNode:
	""" LinkedListNode class 

		> Sufficient to create a liked list (in main)
	"""
	def __init__(self, data):
		""" Initializes a node in a linked list *with 'data' as only argument*
			(we will set 'next' to None for now)
			(Has to be generated after creating the nodes)
		"""
		self.data = data
		self.next = None

	def __repr__(self):
		""" String """
		return f"<{self.data}::{self.next}>"

	def print_all(self):
		""" prints all nodes, starting from the roots """
		curr = self
		while curr.next:
			print(curr)
			curr = curr.next
		print(curr) # Last thing in list - next is None



	# if __name__ == '__main__':

	# 	# Create the nodes
	# 	l0 = LLNode('first')
	# 	l1 = LLNode('sec')
	# 	l2 = LLNode('thi')

	# 	# print(l0, l1, l2)

	# 	# Link them all together by setting their pointers
	# 	l0.next = l1
	# 	l1.next = l2

	# 	# Call print function to print all 
	# 	l0.print_all()


class LinkedList:
	""" Uses LLNode objects and their methods to link them together


	"""
	def __init__(self):
		""" 
		To exist, a linked list must have a head.
		If list is empty, set head to None.

		# Adding a tail attribute makes appending easier
		# because we 'know' it - O()
		# Otherwise, need to walk to the end and add it there
		"""
		self.head = None # Empty list []
		self.tail = None

	def print_LList(self):
		
		curr = self.head
		# self.head.print_all() # Either use the built in LLNode function

		# Or, walk through the list with this class:
		while curr is not None:
			print(curr.data, curr)
			curr = curr.next


	def append_node(self, data):
		""" Append a node with data to the end of the list

			Optimized to take (O(1)) because we stored 'tail'
		"""
		print('adding node', data)
		new_node = LLNode(data)

		if self.head is None:
			self.head = new_node

		if self.tail is not None:
			self.tail.next = new_node

		self.tail = new_node

	def push(self, data):
		""" Push a node with data to the front of the list

			Does not matter if list is empty or not 
				(if self.head is None)
			The new node has to do two things:
			- become the next head
			- push the former head out of the way by setting it as nn.next

			Takes (O(1)) linear time


		"""
		nn = LLNode(data)

		nn.next = self.head
		self.head = nn 
		


# if __name__ == '__main__':
	# ll = LinkedList()
	# # print(ll, 'head', ll.head)

	# ll.append_node(1)
	# ll.append_node(2)
	# ll.append_node(3)

	# ll.print_LList()












class DLNode:
	

	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

	def __repr__(self):
		return f'Node {self.data}'

	def print_all(self):
		print(f'Printing all starting with {self.data}')

		curr = self

		while curr.next:
			print(f'{curr.data} :: pv {curr.prev} :: nx {curr.next}')
			curr = curr.next

		print(f'{curr.data} :: pv {curr.prev} :: nx {curr.next}')

	def search_for_data(self, data):
		print('searching for ', data)
		curr = self
		while curr.next:
			if curr.data == data:
				return curr

			else:
				curr = curr.next
		return 'Not Found'


class DoublyLinkedList:
	"""Doubly linked list 
		
		Diffs to reg linked list : we do not need a tail because we have the 
		ability to find any item in O(1) time!

	"""

	def __init__(self):
		""" Empty list """
		self.head = None

	def printLL(self):
		if self.head:
			self.head.print_all()
		else:
			print('[]')


	def insert_at_end(self, data):
		""" Inserts a new node to the end """
		new_node = DLNode(data)
		if self.head == None: # empty list
			self.head = new_node

		elif self.head != None: # 1 or more more items in list
			# Start at head and traverse until we get to the end

			curr = self.head
			while curr.next:
				curr=curr.next

			#Then add to the end.
			curr.next = new_node
			new_node.prev = curr

		self.printLL()


	def insert_at_start(self, data):
		nn = DLNode(data)

		
		if self.head == None:   # empty list
			self.head = nn
		else:                   # Nonempty list
			old_head = self.head
			self.head = nn
			old_head.prev = self.head # Set the pointers
			self.head.next = old_head

			



		self.printLL()




if __name__ == '__main__':

	DLL = DoublyLinkedList()
	# DLL.printLL()
	# DLL.insert_at_end(99)
	# DLL.insert_at_end(88)
	# DLL.insert_at_end(77)
	# DLL.insert_at_end(66)

	DLL.insert_at_start(188)
	DLL.insert_at_start(177)
	DLL.insert_at_start(166)





	# dl0 = DLNode('0') # Head
	# # dl0.print_all()
	# # print(dl0.next, dl0.prev)

	# dl1 = DLNode('1') # 0 -> 1
	# dl0.next = dl1
	# dl1.prev = dl0


	# dl2 = DLNode('2') # 0 -> 1 -> 2
	# dl1.next = dl2
	# dl2.prev = dl1

	# dl3 = DLNode('3') # 0 -> 1 -> 2
	# dl2.next = dl3
	# dl3.prev = dl2

	# dl0.print_all()

	# print(dl0.search_for_data('2'))
















































































































































