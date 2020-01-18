# Stacks & Queues Ch3 : Interview Questions
# Base class:
class Queue:
	""" A basic Queue example ... 
		
		>>> q = Queue()
		>>> print(q.get_min_element())
		Empty queue
		>>> q.push(1)
		[1]
		>>> q.push(2)
		[1, 2]
		>>> q.push(0)
		[1, 2, 0]
		>>> q.size()
		3
		>>> print(str(q))
		[1, 2, 0]
		>>> q.get_min_element()
		0
		>>> q.pop()
		[2, 0]

	"""

	def __init__(self):
		# Constructor creates a list
		self.queue = []
	
	def __repr__(self):
		# Constructor creates a list
		return str(self.queue)
	
	def push(self, data):
		# Might check to avoid duplicate entries?
		self.queue.append(data)
		print(self.queue)

	def pop(self):
		# Remove last elem from queue
		if len(self.queue) > 0:
			self.queue.pop(0)
			print(self.queue)
		else:
			print('Illegal')

	def size(self):
		# Get the size of the queue
		return len(self.queue)

	"""
	3.2 queue Min: How would you design a queue which, in addition to push and pop, has a function min
	which returns the minimum eiement? Push, pop and min should ail operate in 0(1) time.
	"""
	def get_min_element(self):
		sz = self.size()
		if sz > 0:
			mn = self.queue[0]
			for i in range(1, sz):
				if self.queue[i] < mn:
					mn = self.queue[i]

		else:
			return 'Empty queue' 
		return mn


# Base class:
class Stack:
	""" A basic Stack example ... 
		
		>>> s = Stack()
		>>> print(s.get_min_element())
		Empty stack
		>>> s.push(1)
		[1]
		>>> s.push(2)
		[1, 2]
		>>> s.push(0)
		[1, 2, 0]
		>>> s.size()
		3
		>>> print(str(s))
		[1, 2, 0]
		>>> s.get_min_element()
		0

	"""

	def __init__(self):
		# Constructor creates a list
		self.stack = []
	
	def __repr__(self):
		# Constructor creates a list
		return str(self.stack)
	
	def push(self, data):
		# Might heck to avoid duplicate entries?
		self.stack.append(data)
		print(self.stack)

	def pop(self):
		# Remove last elem from stack
		if len(self.stack) > 0:
			self.stack.pop()
		else:
			print('Illegal')

	def size(self):
		# Get the size of the stack
		return len(self.stack)

	"""
	3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
	which returns the minimum eiement? Push, pop and min should ail operate in 0(1) time.
	"""
	def get_min_element(self):

		
		sz = self.size()
		# print(self.stack, sz)
		if sz > 0:
			mn = self.stack[0]
			for i in range(1, sz):
				if self.stack[i] < mn:
					mn = self.stack[i]

		else:
			return 'Empty stack' 
		return mn


	
# 3.1	Three in One: Describe how you could use a single array to implement three stacks.
class ThreeStacks():
	""" 
	Hints: 
	#12 - We could simulate three stacks in an array by just allocating the first third of the array to
		the first stack, the second third to the second stack, and the final third to the third stack.
		One might actually be much bigger than the others, though. Can we be more flexible with the divisions? 
		If you want to allow for flexible divisions, you can shift stacks around. Can you ensure that all available capacity is used? 
	#58 - Try thinking about the array as circular, such that the end of the array "wraps around" to the start of thearray
	# >>> three_in_one()

	"""
	def __init__(self):
		self.array = [None, None, None]
		self.current = [0, 1, 2]

	def push(self, item, stack_number):
		if not stack_number in [0, 1, 2]:
			raise Exception("Bad stack number")
		
		while len(self.array) <= self.current[stack_number]:
			self.array += [None] * len(self.array)
		
		self.array[self.current[stack_number]] = item
		self.current[stack_number] += 3

	def pop(self, stack_number):
		if not stack_number in [0, 1, 2]:
			raise Exception("Bad stack number")
		
		if self.current[stack_number] > 3:
			self.current[stack_number] -= 3
		
		item = self.array[self.current[stack_number]]
		self.array[self.current[stack_number]] = None
		return item





"""
3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStack s that mimics this. SetOfStack s should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStack s .push() and SetOfStack s .pop() should behave identically to a single stack
(that is, pop( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt( in t index ) which performsa pop operation on a specific sub-stack.
Hints: #64, #81
"""
"""
3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
Hints: #98, #114
"""
"""
3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
Hints: #15, »32,043
"""
"""
3.6 Animal Shelter
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat.You may use the built-in LinkedLis t data structure.
Hints: #22, #56, #63 

"""




if __name__ == "__main__":
	import doctest
	doctest.testmod()
