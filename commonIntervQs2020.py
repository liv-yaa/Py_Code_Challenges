"""
Common interview questions
# From hackernoon https://hackernoon.com/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0

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
		How do you find the missing number in a given integer array of 1 to 100? (solution)
		How do you find the duplicate number on a given integer array? (solution)
		How do you find the largest and smallest number in an unsorted integer array? (solution)
		How do you find all pairs of an integer array whose sum is equal to a given number? (solution)
		How do you find duplicate numbers in an array if it contains multiple duplicates? (solution)
		How are duplicates removed from a given array in Java? (solution)
		How is an integer array sorted in place using the quicksort algorithm? (solution)
		How do you remove duplicates from an array in place? (solution)
		How do you reverse an array in place in Java? (solution)
		How are duplicates removed from an array without using any library? (solution)
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

SQL:
	- Write SQL query to find second highest salary in employee table? (solution)
		SELECT MAX(Salary) FROM Employee WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee)


Bitwise:
	- How do you find if a number is a power of two, without using arithmetic operator?
		return (x & (x - 1)) == 0


Command line / UNIX
	- How do you find a  running Java process on UNIX? (command)
		You can use the combination of 'ps' and 'grep' command to find any process running on UNIX machine.
		ps -ef | grep "myApp"


"""






















































































































































































































































































































































































