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


















