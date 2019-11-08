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
    s, i, m = [], 0, 0
    while i < len(H):
    	if not s or H[i] > H[s[-1]]:
    		s.append(i)
    		i += 1
		else:
			t = s.pop()
			a = H[t] * ((i - s[-1] - 1) if s else i)
			if a > m:
				m = a

	while s:
		t = s.pop()
		a = H[t] * ((i - s[-1] - 1) if s else i)
		if a > m:
			m = a

	return m






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
    print(
		f"""Array is sorted in {ct} swaps.  
		First Element: {a[0]} 
		Last Element: {a[-1]} 
		""" 
    )


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
    def quicksort(lst):
        if len(lst) < 2: #base case
            return lst

		pivot = lst[int(len(lst) / 2)]

		lo = [e for e in lst if e < pivot]
		eq = [e for e in lst if e == pivot]
		hi = [e for e in lst if e > pivot]
        
        return quicksort(lo) + eq + quicksort(hi)

    d = []
    for item in quicksort(prices):
        if sum(d) + item <= k:
            d.append(item)
    return len(d)




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

	def findDFS(self, data):
		"""
		Depth-first search for a node(DFS) - a STACK!
		We search the children of the current node before the next 
		sibling of the current node, then go the second
		Could also use recursion
		"""

		# Initialze a list with values we need to visit
		to_visit = [self]

		while to_visit: # While we still have chilrent nodes
			curr = to_visit.pop()

			if curr == data:
				return curr # Return the current TreeNode

			else:
				# Add all of the current children to the list we want to visit
				to_visit.extend(curr.children)


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

			if curr.data = data:
				return curr

			to_visit.extend(curr.children)















































