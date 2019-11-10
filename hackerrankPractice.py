# hackerrank practice

# Stacks & Queues
# https://www.hackerrank.com/rest/contests/master/challenges/balanced-brackets/hackers/zhangsen1121/download_solution
import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(0)
        elif c == ')':
            if len(stack) > 0 and stack[-1] == 0:
                stack.pop()
            else:
                return 'NO'
        
        if c == '[':
            stack.append(1)
        elif c == ']':
            if len(stack) > 0 and stack[-1] == 1:
                stack.pop()
            else:
                return 'NO'
        
        if c == '{':
            stack.append(2)
        elif c == '}':
            if len(stack) > 0 and stack[-1] == 2:
                stack.pop()
            else:
                return 'NO'

    if stack == []:
        return 'YES'
    else:
        return 'NO'

# Hackbright
class Stack(object):
	""" Stack using a list """
	def __init__(self):
		self._stack = []

	def push(self, item):
		# Add item to top/end
		self._stack.append(item)

	def pop(self):
		# Remove top/end item
		return self._stack.pop()

	def peek(self):
		# Return, dont remove, top item
		return self._stack[-1]

	def is_empty(self):
		return not self._stack



class Queue(object):
	""" Queu using a list - could be fster with Linked list """
	def __init__(self):
		self._queue = []

	def push(self, item):
		# Add item to top/end
		self._queue.append(item)

	def pop(self):
		# Remove first/bottom item
		return self._queue.pop(0)

	def peek(self):
		# Return, dont remove, first/bottom item
		return self._queue[0]

	def is_empty(self):
		return not self._queue



# Alternative way to make a queue
import collections
dq = collections.deque()
dq.append('hi')
dq.pop()
    # q.append(3)
    # q.append(4)
    # q.pop()
    # print(q)



def solve(H) :
    pass
 #    s, i, m = [], 0, 0
 #    while i < len(H):
 #    	if not s or H[i] > H[s[-1]]:
 #    		s.append(i)
 #    		i += 1
	# 	else:

	# 		t = s.pop()
	# 		a = H[t] * ((i - s[-1] - 1) if s else i)
	# 		if a > m:
	# 			m = a

	# while s:
	# 	t = s.pop()
	# 	a = H[t] * ((i - s[-1] - 1) if s else i)
	# 	if a > m:
	# 		m = a

	# return m






# Terminated due to timeout :(
# /**
# *   Worst: O(n) algorithm
# *     Checks if n is divisible by any number from 4 to n.
# *
# *   @param n An integer to be checked for primality.
# *   @return true if n is prime, false if n is not prime.
# **/
def primalityBad(n):
    facs = [i for i in range(1, n + 1) if n % i == 0]
    print(facs)

    if len(facs) == 2:
        return 'Prime'
    return 'Not prime'


# /**
# *   O(n^(1/2)) Algorithm
# *    Checks if n is divisible by any number from 2 to sqrt(n).
# *
# *   @param n An integer to be checked for primality.
# *   @return true if n is prime, false if n is not prime.
# **/
import math
def btrPrimality(n):
	count = 0
	if n == 1:
		return False
	elif n == 2:
		return True

	for i in range(2, math.ceil(math.sqrt(n)) + 1): # Go up to sqrt, only odds
		count += 1
		if (n % i == 0):
			# print(count)
			return False

	#n is prime
	return True


# ~~ STRING MANIPULATION ~~ 

def alternatingCharacters(s):
    return len([i for i in range(len(s) - 1) if s[i] == s[i + 1]])

# ~ Slow :(
# Complete the commonChild function below.
def commonChild(s1, s2):
    # in order, delete 0 or more chars

    c1 = set([s1])
    c2 = set([s2])
    c = set()
    for i in range(len(s1), -1, -1 ):
        com1 = combinations(s1, i)
        com2 = combinations(s2, i)

        for j in com1:
            c1.add(''.join(j))

        for j in com2:
            c2.add(''.join(j))

    c = c1.intersection(c2)
    print(c1)
    print(c2)

    l = [len(k) for k in c]
    return max(l)





# Make anagrams
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a = Counter(a)
    b = Counter(b)

    print(a, b)
    c = a - b
    d = b - a
    e = c + d # outliers

    return len(list(e.elements()))


# Time out : Complete the whatFlavors function below.
def whatFlavors(cost, money):
    ic = (0, 0)
    
    for i in range(len(cost) - 1):
        for j in range(len(cost) - 1):
            if cost[i] + cost[j] == money and i != j:
                ic = (min(i + 1, j + 1), max(i + 1, j + 1))
    
    print(ic[0], ic[1])



# Still slow
def whatFlavors(cost, money):
    ic = (0, 0)
    
    for c in combinations(range(len(cost)), 2):
        if cost[c[0]] + cost[c[1]] == money and c[0] != c[1]:
            ic = (min(c[0] + 1, c[1] + 1), max(c[0] + 1, c[1] + 1))
    
    print(ic[0], ic[1])



# answer to whatFlavors function below.
def whatFlavors(a, m):
    prices = {}
    for idx, p in enumerate(a):
        if m - p in prices:
            print(prices[m - p] + 1, idx + 1)
        prices[p] = idx


#Thus, the key to solving this challenge is determining whether or not the two strings share a common character because if they have a common character then they have a common substring of lengh 1.
#To do this, we create two sets,  and , where each set contains the unique characters that appear in the string it's named after.
def twoStrings(s1, s2):
    if set(s1) & set(s2):
        return 'YES'
    return 'NO'




# Complete the countSwaps function below.
def countSwaps(a):
    ct = 0
    while a != sorted(a):
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                ct += 1
  #   print(
		# f"""Array is sorted in {ct} swaps.  
		# First Element: {a[0]} 
		# Last Element: {a[-1]} 
		# """ 
  #   )

# QUICKSORT O(nlogn)
#sorting-demo/quick.py
def quicksort(lst):
	""" Quicksort from HB lecture
		O(n log(n)) time 
	"""
	if len(lst) < 2: #base case
		return lst

	# Select pivot element
	pivot = lst[int(len(lst) / 2)]

	# Partition elems into lo, hi, eq buckets
	lo = [e for e in lst if e < pivot]
	eq = [e for e in lst if e == pivot]
	hi = [e for e in lst if e > pivot]
	
	# Recursive call - concatenate buckets
	return quicksort(lo) + eq + quicksort(hi)


#https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting&isFullScreen=true
def maximumToys(prices, k):
    # HB lec - recursive quicksort

    d = []
    for item in quicksort(prices):
        if sum(d) + item <= k:
            d.append(item)
    return len(d)



"""
# MERGESORT O(nlog(n))
# Has two steps:
    1. Break down everything into a list of one
    2. Compare the frirst items of each pair of lists & interleave

"""

def merge_sort(lst):
    """ Mergesort list and return result """

    # 1; Break down everything into a list of one
    if len(lst) < 2:
        return lst 

    mid = int(len(lst) / 2)
    ls1 = merge_sort(lst[:mid]) # divide list in half
    ls2 = merge_sort(lst[mid:]) # the other half

    return make_merge(lst1, lst2)

def make_merge(lst1, lst2):
    """ """

    # 2. Compare the first items of each pair of lists & interleave

    result_list = []

    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2 == []:
            result_list.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            result_list.append(lst1.pop(0))
        else:
            result_list.append(lst2.pop(0))

    return result_list



from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
    	self.name = ""
        self.score = 0
        print('repr', self.name, self.score)
        
    def comparator(a, b):
        # Sorts in descending order so switched
        if a.score < b.score:
            return 1
        if a.score == b.score:
            # Sort by ascending name
            if a.name > b.name:
                return 1
            else:
                return -1
        if a.score > b.score:
            return -1


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)





# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort() # Now we know the result dist for adjacent values will always be positive!
    minn = abs(arr[0] - arr[-1])

    for i in range(len(arr) - 1):
        dis = abs(arr[i] - arr[i + 1])
        if dis < minn:
            minn = dis

    return minn



# TREES - from HB

class TreeNode(object):
	""" from HB lecture """

	def __init__(self, data, children=None):
		self.data = data
		self.children = children

	def __repr__(self):
		print(self.data, self.children)

	def find(self, data):
		"""
		Depth-first search for a node(DFS) - a STACK!
		We search the children of the current node before the next 
		sibling of the current node, then go the second
		Could also use recursion
		"""

		# Initialze a list with values we need to visit
		to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                # return current
                pass

            to_visit.extend(current.children)


	def findBFS(self, data):
		"""
		Breadth-first search for a node(BFS) - a QUEUE!
		We search the children of the current node before the next 
		sibling of the current node, then go the second
		Could also use recursion
		"""

		to_visit = [self]

		while to_visit:
			curr = to_visit.pop(0) # Popping from the front makes it a queue

			if curr.data == data:
				return curr

			to_visit.extend(curr.children)


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root={root}>".format(root=self.root)

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.findBFS(data)
        # return self.root.findDFS(data)
    	

# if __name__=='__main__':
#     # Make an example tree and search for things in it

#     res = TreeNode("r.txt", [])
#     mes = TreeNode("m.txt", [])
#     jan = TreeNode("jan/", [res, mes])
#     ser = TreeNode("ser.py", [])
#     jes = TreeNode("jes/", [ser])
#     use = TreeNode("Users/", [jan, jes])
#     root = TreeNode("/", [use])

#     tree = Tree(root)
#     print(tree)

#     print(tree.find_in_tree("ser.py")) # True - found it
#     print(tree.find_in_tree("s.css")) # Fasle - not here



class Node:
    """ Tree node from HackR https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=trees&isFullScreen=true"""
    def __init__(self, info):
        self.info = info
        self.right = None
        self.left = None
        self.level = None

    def __str__(self):
        return str(self.info)


    def height(root):
        pass

class BinarySearchTree:
    """ BST from HackR https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=trees&isFullScreen=true"""
    def __init__(self):
        self.root = None

    def create(self, val):
        # Create the root if not yet exists
        if self.root == None:
            self.root = Node(val)
        else:
            curr = self.root
         
            while True:
                if val < curr.info:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(val)
                        break
                elif val > curr.info:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(val)
                        break
                else:
                    break

def height(root):
    if root == None:
        return -1
    else:
        return 1 + max ( height(root.left) , height(root.right))



def findLCA(root, v1, v2):
    """ 
    https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/editorial?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=trees&isFullScreen=true
    Find the least common ancestor 
    case 1 : 
        Both v1 and v2 are on the right of the current root
    case 2 : 
        Both v1 and v2 are on the left of the current root
    case 3 (terminal case):
        v1 and v2 are on diff subtrees or one of them is current root


    """
    # Make sure they are in the right order
    if v1 > v2:
        v1, v2 = v2, v1

    # Traverse until terminal
    while True:
        if v1 < root.info and v2 < root.info:
            root = root.left
        elif v1 > root.info and v2 > root.info:
            root = root.right
        else:
            return root


# ** RECURSION 
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



# ** Linked Lists

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data): 
        node = SinglyLinkedListNode(node_data) #create a node

        if not self.head:
            self.head = node # Initialize the head node if empty

        else:
            self.tail.next = node # otherwise set pointer to point at new node

        self.tail = node # update the tail to be the node

    def print_singly_linked_list(node, sep, fptr):
        while node:
            fptr.write(str(node.data))

            node = node.next

            if node:
                fptr.write(sep)

    def print_list(self):
        """Print all items in the list."""

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def find(self, data):
        """Does this data exist in our list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def insertNodeAtPosition(head, data, position):
        node = head

        # make the insertion at the head
        if position == 0:
            newNode = SinglyLinkedListNode(data)
            newNode.next = head # make it point to previous head
            return newNode

        count = 1

        # Breaks when we are at end and node.next = None
        # or, when we get to the position
        while count < position and node:
            count += 1
            node = node.next


        # WE are now at the position we want
        # `node` is the one we are 'bumping over'
        newNode = SinglyLinkedListNode(data) # create new node
        newNode.next = node.next # set next to this nodes next
        node.next = newNode # update the pointer of the old one
        
        return head # 

    def has_cycle(head):
        # I did this HR prob!!! :D
        #has_cycle has the following parameter(s):
        # head: a pointer to a Node object that points to the head of a linked list
        # A random linked list is generated at runtime and passed to your function.
        
        curr = head
        seen = []
        while curr:
            seen.append(curr)
            if curr.next in seen:
                # Found a loop
                return True
            curr = curr.next
            
        return 


    def FindMergeNode(headA, headB):
        out = []
        while headA:
            out.append(headA)
            headA = headA.next
            
        while headB:
            if headB in out:
                return headB.data
            headB = headB.next
        
        return None
        


# Doubly linked list
#https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists&isFullScreen=true

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node

        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


    def print_doubly_linked_list(node, sep, fptr):
        while node:
            fptr.write(str(node.data))

            node = node.next

            if node:
                fptr.write(sep)


    def sortedInsert(head, data):
        """ create a new DoublyLinkedListNode object having data value  and insert it into a sorted linked list while maintaining the sort.
        """
        # Create new node
        n = DoublyLinkedListNode(data)

        # If empty list
        if head == None:
            n.next = self.head
            self.head.next = n.next
            self.head = n

        # At beginnig of list
        elif head.tail == null:

            pass

        # At middle of list


        # At end of list










# GREEDY ALGOS
# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    cost = 0
    frs = {i:0 for i in range(k)}

    while True:
        for f in frs:
            if len(c) == 0:
                return cost
            p = c.pop(0)
            pr = ((frs[f] + 1) * p)
            cost += pr
            frs[f] = frs[f] + 1



# WROng
def maxMin(k, arr):
    minn = abs(arr[1] - arr[0])
    print(minn)
    for c in combinations(arr, k):
        # print(c)
        un = max(c) - min(c)
        # print(un)
        if un < minn:
            minn = un
    return minn







# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    return min(arr[i + k - 1] - arr[i] for i in range(0, len(arr) - k + 1))



# Complete the pairs function below.
def pairs(k, arr):
    vals = {x : 1 for x in arr}
    answer = 0
    for c in arr:
        try:
            if vals[c - k]:
                answer += 1
        except:
            continue
    return answer


## RECURSION

# Works for small numbers - Complete the superDigit function below.
def superDigit(n, k):

    d = n * k
    if d // 10 == 0:
        return d

    else:
        s = sum([int(c) for c in str(d)])
        print(s)
        return superDigit(s, 1)


        

# Ways to make recursion faster:
# - memoization
# - dynamic programming - store result in array; when you call, check in your array if it already exists



# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            sums.append(sum(arr[i][j:j + 3]) + arr[i + 1][j+1] + sum(arr[i + 2][j:j + 3]))
    return max(sums)


# Complete the rotLeft function below.
def rotLeft(a, d):
    # List slicing is O(k) where k is the slice size
    # This would be appropriate where k << len(lst)
    return a[d:] + a[:d]

""" collections.deque()
A deque is a double-ended queue. It can be used to add or 
remove elements from both ends.

O(1)

Deques support thread safe, memory efficient appends and 
pops from either side of the deque with approximately the 
same  performance in either direction.

You can do cool tasks with deque:

    deq.rotate(-k)
    # rotates the same as rotLeft function

However, note that creating the copy of the list will be O(n) anyway.

"""


#Minimum Swaps 2 - https://www.hackerrank.com/challenges/minimum-swaps-2/editorial?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays&isFullScreen=true
# Editorial:
    # The idea is that if  occupies  position,  occupies  position 
    # and so on, then there will be some integer  which will occupy  position. 
    # So, this forms a cycle.
    # So, if any element i is not at its correct position, we shift it 
    # to its correct position j, then shift j to its correct position k and so on.
    # So, if  is the length of the cycle (number of elements in the cycle), 
    # then it will require a minimum of len - 1 swaps to rearrange the elements of 
    # the cycle to their correct positions.
    # We find all such cycles and compute our answer.
    #The correct positions of all the elements can be found by sorting the array 
    # by value and keeping track of the old and new positions. 

# Doesnt work for larger test cases
def minimumSwaps(arr):
    count = 0

    for i in range(len(arr)):
        min_index = i 
        for j in range(i + 1, len(A)):
            if arr[min_index] > arr[j]:
                min_index = j
        if min_index > i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            count += 1

    return count


# Need to create graphs and return the number - 1

# I was able to prove this with graph-theory. Might want to add that tag in :)

# Create a graph with n vertices. Create an edge from node n_i to n_j if the element in position i should be in position j in the correct ordering. You will now have a graph consisting of several non-intersecting cycles. I argue that the minimum number of swaps needed to order the graph correctly is

# M = sum (c in cycles) size(c) - 1
# Take a second to convince yourself of that...if two items are in a cycle, one swap can just take care of them. If three items are in a cycle, you can swap a pair to put one in the right spot, and a two-cycle remains, etc. If n items are in a cycle, you need n-1 swaps. (This is always true even if you don't swap with immediate neighbors.)

# Given that, you may now be able to see why your algorithm is optimal. If you do a swap and at least one item is in the right position, then it will always reduce the value of M by 1. For any cycle of length n, consider swapping an element into the correct spot, occupied by its neighbor. You now have a correctly ordered element, and a cycle of length n-1.

# Since M is the minimum number of swaps, and your algorithm always reduces M by 1 for each swap, it must be optimal.

#https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
def minimumSwaps(arr):
    arrpos = [[i, j] for i, j in enumerate(arr)] 
    arrpos.sort(key=lambda it:it[1])
    print(arrpos)
    
    # To keep track of visited elements.  
    vis = {k : False for k in range(n)}
    ans = 0

    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            # Already at correct position
            continue
        
        # Find num of nodes in this cycle and add it to ans
        cycle_size = 0
        j = i
        while not vis[j]:
            # mark node as viisted
            vis[j] = True

            # move to next node
            j = arrpos[j][0]
            cycle_size += 1

        # Update answer by adding current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)

    return ans



# Dictionary best practices:
# Use dict.get(key[, default]) to assign default values
def low2():
    nstd = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nstd[score] = nstd.get(score, []) + [name]
    s = sorted(nstd.keys())

    try:
        for n in sorted(nstd[s[1]]):
            print(n)
    except:
        print('error')













