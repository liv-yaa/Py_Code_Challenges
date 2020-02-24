""" ** Common interview questions - prepping for Nylas, Figma, Plenty Jan 2020
https://hackernoon.com/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0

All Data Structures:
	- Array
	- LinkedList
	- Tree
	- Graph
	- Map
	- Vector
	- Matrix
	- DataFrame (Table)
	- Lists 
	- 

Other Topics:
	- SQL
	- Time Complextiies
	- Bitwise
	- Command line / UNIX

"""

"""
Arrays! - common problems: 
	Features:
		- Linear (1D) data structure
		- Size is fixed, storage is contiguous
		- To create a new array, copy the whole thing
		- Fast (O(1)) search if you know the index
		- Slow adding & removing element
		- 

	Questions:
		How do you find all pairs of an integer array whose sum is equal to a given number? (solution)
		How do you find duplicate numbers in an array if it contains multiple duplicates? (solution)
		How are duplicates removed from a given array in Java? (solution)
		How is an integer array sorted in place using the quicksort algorithm? (solution)
		How do you remove duplicates from an array in place? (solution)
		How do you reverse an array in place in Java? (solution)
		How are duplicates removed from an array without using any library? (solution) 
"""
from itertools import combinations, permutations
from copy import deepcopy
import math

class ArrayMethods:

	def missing_num_array_sum2(self, arr):
		""" 
		Find the missing number in a given integer array of 1 to 100.
		`Algorithm 1. ` - O(n)
			Calculate the sum of the array
			Iterate through n's 1-100, subtracting from sum. return what is left.
		"""
		s = sum(arr)
		for n in range(1, 101):
			s -= n
		return -(s)

	# def missing_num_array_sum2(self, arr):
	# 	s = sum(arr)
	# 	for n in range(1, 101):
	# 		s -= n
	# 	return -(s)

	def missing_num_array_sum1(self, arr):
		""" 
		Find the missing number in a given integer array of 1 to 100.
		`Algorithm 1. ` - O(n)
			Calculate the sum of the array
			Iterate through n's 1-100, subtracting from sum. return what is left.
		"""
		n = len(arr)
		total = (n + 1) * (n + 2) / 2
		return int(total - sum(arr))


		# n = len(arr)
		# total = (n + 1) * (n + 2) / 2
		# return int(total - sum(arr))



	def missing_num_array_xor(self, a):
		""" 
		Find the missing number in a given integer array of 1 to 100.
		`Algorithm 3. ` - O(n)
			XOR all the array elements, let the result of XOR be X1.
			XOR all nums from 1 to n, let XOR be X2
			XOR of X1 and X2 gives the missing number.
		"""
		n = len(a)
		x1 = a[0]
		x2 = 1

		for i in range(1, n):
			x1 = x1 ^ a[i]
			# print(x1)

		for i in range(2, n + 2):
			x2 = x2 ^ i

		return x1 ^ x2


		## 

		# n = len(a)
		# x1 = a[0]
		# x2 = 1

		# for i in range(1, n):
		# 	x1 = x1 ^ a[i]
		# 	print(x1)

		# for i in range(2, n + 2):
		# 	x2 = x2 ^ i

		# return x1 ^ x2 


	def find_dup_num_array(self, a, n):
		"""
		Find the duplicate number on a given integer array 

		where a is the array and n is the maximum number? OR the lenght. ..?

		Best - O(n)

		"""

		sm = sum(a)  # get sum of all items in a

		# Go through all items in list, subtracting from the sum
		for i in range(1, n + 1):
			sm -= i 
		return sm # Final value wil be the number you know is a duplicate




	def find_two_dup_num_array(self, arr):
		"""
		Find two duplicate numbers on a given integer array 

		Best if you use a count dictionary - O(n)
		"""
		size = len(arr)
		count = [0] * size
		# print()


		for i in range(0, size):
			if count[arr[i]] == 1:
				print(arr[i], end = ' ')
			else:
				count[arr[i]] = count[arr[i]] + 1

	def find_al_sum_pairs(self, arr, sum):
		""" Find all pair whos sum is equal to n

		 """
		m = [0] * 100 # A general purpose map to store counts of all values in arr
		for i in range(0, len(arr)):

			# Interesting syntax, you get the value, then you are able to add one to it:
			m[arr[i]]
			m[arr[i]] += 1
		print(m)




	def printRepeating(self, arr):
		# print all repeating elements

		# DUmmylist
		count = [0] * len(arr) 

		# Iter through items in the array and add to hte respective 
		for i in range(len(arr)): 
			if count[arr[i]] == 1:
				print(arr[i], end = ' ')
			else:
				count[arr[i]] = count[arr[i]] + 1


		# count = [0] * len(arr)
		# for i in range(len(arr)):
		# 	if count[arr[i]] == 1:
		# 		print(arr[i], end= ' ')
		# 	else:
		# 		count[arr[i]] = count[arr[i]] + 1

	def makeListNondecreasing(self, arr):
		# Overall gaol: Make list nondecreasing by changing only one digit from the array
		# Function to get the nondecreasing list
		myList = [0]
		possible = True # Flag to start by assuming it is possible to make list nondecreasing
		print(myList)

		for i in range(len(arr)):
 			# to fill myList, call helper function 'getBest' with last item 
 			# of myList as prev and arr[i] as curr:
			myList.append(self.getBest(myList[-1], arr[i]))

			if myList[-1] == -1: # We were not able to find it
				possible = False
				break
		return possible

		# ##
		# myList = [0]
		# possible = True

		# for i in range(len(arr)):
		# 	myList.append(self.getBest(myList[-1], arr[i]))

		# 	if myList[-1] == -1:
		# 		possible = False
		# 		break

		# return possible

	def getBest(self, prev, curr):
		# Return the minimum element from the range [prev, MAX]
		# such that it differs in at most 1 digit with cur
		DIGITS = 4
		MIN = 1000
		MAX = 9999
		maximum = max(MIN, prev)

		for i in range(maximum, MAX + 1):
			# Count the number of different digits
			cnt = 0
			# a = i;
			# b = curr

			for k in range(DIGITS):
				if (i % 10 != curr % 10):
					cnt += 1
				# Eliminate the last digits in both numbers:
				i //= 10
				curr //= 10

			if cnt == 0 or cnt == 1:
				return i # We found at most one different digit

		return -1 # If we can't fine any number less than or equal to 1


		# Get minimum element from the range [prev, MAX]
		# Such that it differs in at most 1 digit with cur

		# DIGITS = 4
		# MIN = 1000
		# MAX = 9999
		# maximum = max(MIN, prev)

		# for i in range(maximum, MAX + 1):
		# 	# Count the number of different digits
		# 	cnt = 0
		# 	a = i
		# 	b = curr

		# 	for k in range(DIGITS):
		# 		if (i % 10 != curr % 10): 
		# 			cnt += 1

		# 		# ELmimniate teh last digits in both nubers

		# 		i //= 10
		# 		curr //= 10

		# 	if cnt == 0 or cnt == 1:
		# 		# WE found at least one different digit
		# 		return 1
		# return -1  # fi we didnt find any nubmer less that or equal to 1



	def getPowerSet(self, mySet):
		""" Uses binary combinations to fill in the powerset """
		powSet = []
		l = len(mySet)
		
		# Run binary numbers 00..0 to 11..1
		for bi in range(int(pow(2, l))):
			bs = "{0:b}".format(bi).zfill(l)
			powSet.append([mySet[i] for i in range(l) if bs[i] == '1'])
		
		return powSet


		# Get power set 

		# powSet = []
		# l = len(mySet)

		# for bi in range(int(pow(2, l))):
		# 	bs = "{0:b}".format(bi).zfill(l)
		# 	powSet.append([mySet[i] for i in range(l) if bs[i] == '1'])

		# return powSet

	def printCombinations(self, a, m):
		""" uses POWER SET 
		# You can cahnge the sign +/- of any element.
		# Print all combinations of array elements such that their sum is divisible by m.
		"""
		
		all_inds = []
		for l in range(len(a) + 1):
			all_inds.extend(list(combinations([_ for _ in range(len(a))], l)))
				
		bs = []
		for ind in all_inds:
			b = deepcopy(a)
			for i in ind:
				b[i] = -b[i]
			if sum(b) % m == 0:
				bs.append(b)

		return bs

		
		

	def dynamicArray(self, n, queries):
		# Followed complicated instructions to process queries https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=true
		seqList = [[]] * n 
		lastAns = 0
		las = []

		for q in queries:
			x, y = q[1], q[2]
			idx = (x ^ lastAns) % n
			seq = seqList[idx]

			if q[0] == 1:
				seqList[idx] = seq + [y]

			elif q[0] == 2:
				lastAns = seq[y % len(seq)]
				las.append(lastAns)
		return las

	def leftRot(arr, d):
		return arr[d:] + arr[:d]

	def is_magic(m):
		""" Determines if a linear list representing a matrix `mat` is magic 
		Rows, columns, and diagonals
		"""
		mat = [m[:3], m[3:6], m[6:]]
		rs = set([sum(mat[i]) for i in range(3)])
		cs = set([sum([mat[j][i] for j in range(3)]) for i in range(3)])
		ds = set([sum([mat[0][0], mat[1][1], mat[2][2]]), sum([mat[0][2], mat[1][1], mat[2][0]])])

		# print(rs, cs, ds)    /s

		return len(rs) == 1 and len(cs) == 1 and len(ds) == 1


	def formingMagicSquare(arr):
		""" Def of MagicSquare:
			An  `n x n ` matrix of distinct positive integers from  to  where the sum of any row, column, 
			or diagonal of length  is always equal to the same number: the magic constant.
			You will be given a  matrix  of integers in the inclusive range [1-9]. 
			* We can convert any digit  to any other digit  in the range  at cost of |a-b|. 
			Convert it into a magic square at minimal cost. Print this cost on a new line.


			Algo:
				1. Find all possible 3x3 magic square
				2. Compute cost of changing s into a known magic square
		"""

		# There are 8 magic squares - check all permutations of [1-9]
		magic = [list(p) for p in permutations(range(1, 10)) if is_magic(p)]

		mini = 2**64
		for brr in magic:
			diff = 0
			for i, j in zip(arr, brr):
				diff += abs(i - j)
			mini = min(diff, mini)
		return mini
if __name__=='__main__':
	from random import randint, shuffle
	ay = ArrayMethods()
	# for r in range(4):
	# 	ran = randint(1, 101)
	# 	print('ran', ran)
	# 	ar = [i for i in range(1, ran)] + [i for i in range(ran + 1, 101)]
	# 	print(ay.missing_num_array_sum1(ar))
	# 	print(ay.missing_num_array_sum2(ar))
	# 	print(ay.missing_num_array_xor(ar))

	# 	ar = sorted([i for i in range(1, 101)] + [ran])
	# 	# print(ar)
	# 	print(ay.find_dup_num_array(ar, 100))
	# 	print(ay.find_two_dup_num_array(arr=[1, 2, 2, 3, 4, 4, 5, 6]))
	# print(ay.find_al_sum_pairs([1, 2, 4, 4, 5, 7, 8], 9))
	# ay.printRepeating(arr=[4, 2, 4, 5, 2, 3, 1] ) 
	# print(ay.makeListNondecreasing(arr=[1095, 1094, 1095]))
	# print(ay.getPowerSet(mySet=['a', 'b', 'c']))
	# print(ay.printCombinations(a=[ 3, 5, 6, 8 ] , m=5) )

	# arr = [2, 3, 4, 10, 40]
	# r = len(arr) - 1
	# print(ay.binarySearch(arr=arr, l=0, r=r, x=10))
	# s1 = [4, 9, 2, 3, 5, 7, 8, 1, 5]
	# print(formingMagicSquare(s1)) # 1

	# s2 = [4, 8, 2, 4, 5, 7, 6, 1, 6]
	# print(formingMagicSquare(s2))




"""
Node:
    a concept that carries on for Tree, LList, and Map
    - as self.data
    	- For LinkedList, only has self.next
    	- for Tree, has self.left, self.right 
    	- for Graph, has 
    	- For Map, has self.child1, self.child2, ...
"""




"""
LinkedList!
	Features:
		- Linear (1D) data structure
		- Each node has at most one 'next' node
		- Size is not fixed
		- Stores items in a non-contiguous way (anywhere!)
		- A linked list is nothing but a list of nodes where each node contains the value stored and the address of the next node.
		- Fast to add and remove elements (O(1))
		- Slow Search (O(n)) 
		- Doubly Linked List lets you traverse the circle in both directions
		- * Stack * 


	Questions:
		- Recursive data structure == know recursion!
		- 
		How do you find the middle element of a singly linked list in one pass? (solution)
		How do you check if a given linked list contains a cycle? How do you find the starting node of the cycle? (solution)
		How do you reverse a linked list? (solution)
		How do you reverse a singly linked list without recursion? (solution)
		How are duplicate nodes removed in an unsorted linked list? (solution)
		How do you find the length of a singly linked list? (solution)
		How do you find the third node from the end in a singly linked list? (solution)
		How do you find the sum of two linked lists using Stack? (solution)

"""
class LLNode:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data




"""
Trees!
	- Heirarchical data
	- First node is Root Node
	- Each node has at most two child nodes
	- Every other node is associated with one parent
	- Binary Search tree = An ordered binary tree, where the value of all nodes in the left tree are less than or equal to node and values of all nodes in right subtree is greater than or equal to the node (e.g. root). It's an important data structure and can be used to represent a sorted structure.
	- 'size'
	- 'depth'
	- 'leaf'
	- 'node'
	- Traversal:
		- Pre-order traversal
		- Post-order traversal
		- In-order traversal 

	Questions:
		How is a binary search tree implemented? (solution)
		How do you perform preorder traversal in a given binary tree? (solution)
		How do you traverse a given binary tree in preorder without recursion? (solution)
		How do you perform an inorder traversal in a given binary tree? (solution)
		How do you print all nodes of a given binary tree using inorder traversal without recursion? (solution)
		How do you implement a postorder traversal algorithm? (solution)
		How do you traverse a binary tree in postorder traversal without recursion? (solution)
		How are all leaves of a binary search tree printed? (solution)
		How do you count a number of leaf nodes in a given binary tree? (solution)
		* How do you perform a binary search in a given array? (solution)
"""
class TreeNode(object):
	"""Node in a tree."""

	def __init__(self, data, children):
		self.data = data
		self.children = children

	def __repr__(self):
		return "<Node {data}>".format(data=self.data)

	def find(self, data):
		""" Return a node object with this data 
		Start wherever you are (self.)
		Return None is not foundn
		"""

		to_visit = [self]

		while to_visit:
			current = to_visit.pop()

			if current.data == data:
				return current

			to_visit.extend(current.children)
class Tree(object):
	""" Tree """
	def __init__(self, root):
		self.root = root

	def find_in_tree(self, data):
		# Uses TreeNode method to find the data
		return self.root.find(data)
if __name__=='__main__':
	# tm = TreeMethods()

	# Create lots of TreeNodes, make an example tree, & search for things in it
	resume = TreeNode("resume.txt", []) 
	recipes = TreeNode("recipes.txt", [])
	jane = TreeNode("jane/", [resume, recipes])
	server = TreeNode("server.py", [])
	jessica = TreeNode("jessica/", [server])
	users = TreeNode("Users/", [jane, jessica])
	root = TreeNode("/", [users])

	tree = Tree(root)
	# print("server.py = ", tree.find_in_tree("server.py"))  # should find
	# print("style.css = ", tree.find_in_tree("style.css"))  # should not find


"""
Maps!
	Features:
		- 


	Questions:
		- Recursive data structure == know recursion!
		- 
"""





"""
Strings!
	Features:
		- An array of characters...
		- Size is fixed, storage is contiguous
		- Fast to add and remove elements (O(1))
		- Slow Search (O(n)) 


	Questions:
		How do you print duplicate characters from a string? (solution)
		How do you check if two strings are anagrams of each other? (solution)
		How do you print the first non-repeated character from a string? (solution)
		How can a given string be reversed using recursion? (solution)
		How do you check if a string contains only digits? (solution)
		How are duplicate characters found in a string? (solution)
		How do you count a number of vowels and consonants in a given string? (solution)
		How do you count the occurrence of a given character in a string? (solution)
		How do you find all permutations of a string? (solution)
		How do you reverse words in a given sentence without using any library method? (solution)
		How do you check if two strings are a rotation of each other? (solution)
		How do you check if a given string is a palindrome? (solution)

"""
class Strings:
	def reverse_list(self, lst):
		# Write a function that takes a list of characters and reverses the letters 
		## ** in place **
		left = 0
		right = len(lst) - 1

		while left < right:
			# Swap, move toward middle:

			lst[left], lst[right] = lst[right], lst[left]

			left += 1
			right -= 1

		return lst

	def reverse_words(self, message):
		"""
		Takes a message as a list of characters and reverses the order of the words in place
		* Space separated

		"""
		# uses the above functoin
		


if __name__=='__main__':
	s = Strings()
	print(s.reverse_list(['a', 'b', 'c']))
	print(s.reverse_words(['abble', 'cobble', 'snob']))





"""
Stacks!
	Features:
		- An array or linkedList
		- methods: push, pop, delete, print

	Questions:
		
"""
class Stack:
	pass




"""
Algorithms:
	- What is time complexity of an algorithm?
		Time complexity specifies the ratio of time to the input (asymptotic approximation)
	- Practical times to use recursive algo?
		Linked Lists, reversing String, calculating Fibonacci series, 
		reversing linkedList, tree traversal, QuickSort
"""
class Algos:
	
	def binarySearch(self, arr, l, r, x):
		""" RECURSIVE
				- Takes arr, an *ordered* array, left, right, and x(the target)
				- Returns the recursive call to smaller and 
				smaller 'windows' (between l & r)

			O(log n) time and O(1) space

		"""
		# Check base case
		if r >= l:

			mid = l + (r - l) // 2 + 1 # Get a discrete (arbitrary) midpoint

			# if element is @ the middle itself, we are done
			if arr[mid] == x:
				return mid

			# If element is smaller / larger than mid, we move window:
			elif arr[mid] > x:
				# recurse on left subarray
				return self.binarySearch(arr, l, mid - 1, x)
			else:
				# recurse on right subarray
				return self.binarySearch(arr, mid + 1, r, x)
		else:
			# When l and r 'cross over', we know element x is not present
			# in the array
			return -1

	# *** Practice this from cake.py!!
	# def mergeSort(lst):
	# 	"""
	# 	https://www.interviewcake.com/article/python/logarithms?course=fc1&section=algorithmic-thinking
	# 	"""

	# 	# Base case: lists w/ 0 or 1 elements are sorted
	# 	if len(lst) < 2:
	# 		return lst

	# 	# Step 1: Divide list in half
	# 	mid_idx = len(lst) / 2
	# 	left = lst[:mid_idx]
	# 	right = lst[mid_idx:]

	# 	# Step 2: Sort each half
	# 	sorted_left = mergeSort(left)
	# 	sorted_right = mergeSort(right)

	# 	# Step 3: Merge the sorted halves
	# 	sorted_list = []
	# 	curr_left = 0
	# 	curr_right = 0

	# 	while len(sorted_list) < len(left) ...









"""
SQL:
	- What is SQL injection?
		A security vulnerability - an intruder can inject SQL code, mess up your queries or steal!
	- What is the difference between an inner join and a left join in SQL? (answer)
		Inner join: 
			Collects all matching records 'overlap' of left and right tables
		Outer join: (can be left or right) 
			Collects all matching records from left table and just matching records from right

	- Write SQL query to find second highest salary in employee table? (solution)
		SELECT MAX(Salary) FROM Employee WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee)


Bitwise, Operators:
	- What is 1 XOR 1? 0 XOR 0?
		0
		Because they are the same, this operator returns zero.
	- What is 1 XOR 0? 0 XOR 1?
		1
		Because they are not the same, this operator returns one.

	- What is difference between & and && operator?
		& is a bitwise operator while && is a logical operator (only usable on boolean values)

	- How do you find if a number is a power of two, without using arithmetic operator?
		return (x & (x - 1)) == 0


Command line / UNIX

	- How do you find a  running Java process on UNIX? (command)
		You can use the combination of 'ps' and 'grep' command to find any process running on UNIX machine.
			ps -ef | grep "myApp"

	- How do you find large files in UNIX  e.g. more than 1GB? (command)
			find . - type f -size +1G -print

	- What is the shell script? 
		A shell script is set of shell commands with some programming constructs e.g. if and for loop, which allow you to automate some repetitive task.

Testing
	- Why create a Mock object?
		A powerful tool for creating automated unit tests. Sets up realistic object to test on.
	- Can you describe three different kinds of testing that might be performed on an application before it goes live?
		unit testing, integration testing and smoke testing.
	- Unit testing is?
		Testing individual functions' functionality (JUnit, Unittest, Jenkins for continuous testing)


OOP
	- What is an Immutable class?
		If state cannot be changed once created (must be totally copied)
		Ex. String 

	- What is the difference between a class and an object? (detailed answer)
		A class is a blueprint on which objects are created.
		A class has code and behavior but an object has state and behavior

	- What is the dfference between an interface and an abstract class?
		An interface is the purest form of abstraction with nothing concrete in place
		An abstract class is a combination of some abstraction and concrete things

	- What is the difference between composition, aggregation, and association? (detailed answer)
		Association means two objects are related to each other but can exist without each other, 
		Composition is a form of association where one object is composed of multiple objects, but they only exists together e.g. human body is the composition of organs, individual organs cannot live they only useful in the body. 
		Aggregation is a collection of object e.g. city is an aggregation of citizens.

Other:
	- What is a strongly typed programming language?
		Java
		The compiler cannot handle multiple data types
	- What is a weakly typed programming language?
		Python, Perl
		ex. you can store a numeric string in a number type
	- What is heap and stack in a process? 
		Heap:
		Stack: 
	- What is the relationship between threads and processes?
		A process can have multiple threads 
		but a thread always belongs to a single process. 

"""






















































































































































































































































































































































































