""" ** Common interview questions From hackernoon https://hackernoon.com/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0

All Data Structures:
	- Array
	- LinkedList
	- Vector
	- Matrix
	- DataFrame (Table)
	- Lists 

Other Topics:
	- SQL
	- Time Complextiies
	- Bitwise
	- Command line / UNIX

"""

"""
Arrays!
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

class Arrays:

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

	def find_dup_num_array(self, a, n):
		"""
		Find the duplicate number on a given integer array 

		Best - O(n)
		"""

		sm = sum(a)
		for i in range(1, n + 1):
			sm -= i 
		return sm

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
		""" Find all pair whos sum is equal to n """
		m = [0] * 100 # A general purpose map to store counts of all values in arr
		for i in range(0, len(arr)):
			m[arr[i]]
			m[arr[i]] += 1
		print(m)

	def printRepeating(self, arr):
		# print all repeating elements
		count = [0] * len(arr)
		for i in range(len(arr)):
			if count[arr[i]] == 1:
				print(arr[i], end = ' ')
			else:
				count[arr[i]] = count[arr[i]] + 1

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


if __name__=='__main__':
	from random import randint, shuffle
	ay = Arrays()

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
	# arr = [4, 2, 4, 5, 2, 3, 1] 
	# ay.printRepeating(arr) 
	arr = [1095, 1094, 1095]
	print(ay.makeListNondecreasing(arr))


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

"""
Binary Tree!
	Features:
		- Heirarchical data
		- Each node has at most two child nodes
		- Binary Search tree - 
			An ordered binary tree, where the value of all nodes in the left tree are less than or equal to node and values of all nodes in right subtree is greater than or equal to the node (e.g. root). It's an important data structure and can be used to represent a sorted structure.
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
		How do you perform a binary search in a given array? (solution)

"""

"""
Algorithms:
	- What is time complexity of an algorithm?
		Time complexity specifies the ratio of time to the input (asymptotic approximation)
	- Practical times to use recursive algo?
		Linked Lists, reversing String, calculating Fibonacci series, 
		reversing linkedList, tree traversal, QuickSort

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






















































































































































































































































































































































































