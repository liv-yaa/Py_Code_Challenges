# recursion.py 
# https://fellowship.hackbrightacademy.com/materials/ft25a/lectures/recursion/

# Demonstration of a call stack
def count_recursive(n=1):
	if n > 3:
		return

	print(n)
	count_recursive(n + 1)


# Find length of list recursively:
def lenlist(lst):
	""""Return length of list using recursion without using len()"""

	if lst == []:
		return 0
	return 1 + lenlist(lst[1:])


# Parse and flatten a challeging list
def doubler_flattener(lst):
    """ Non recursive; hairy
    Print items in flattened list, doubled, for 1 level of nesting"""

    stack = list(reversed(lst))

    while stack:
    	n = stack.pop()
    	if isinstance(n, list):
    		# If it's a list, add it to stack, reversed
    		for inner in reversed(n):
    			stack.append(inner)
		else:
			print(n * 2)
    	

def doubler_recursive(lst):
    """Print items in list doubled, using recursion."""

    for n in lst:
        if isinstance(n, list):
            doubler_recursive(n)
        else:
            print(n * 2)


def doubler_no_loop(lst):
	if not lst:
		return

	n, rest = lst[0], lst[1:]

	if isinstance(n, list):
		doubler_no_loop(n)

	else:
		print(n * 2)

	doubler_no_loop(rest)


# Needs a tree but - 
def list_nodes_recursive(self, node):
    print(node.data)
    for child in node.children:
        list_nodes_recursive(child)


# Indenting recursive - for Filesystem navigation!
def indent_list(node, depth=0):
    """List all nodes, indented."""
    print("  " * depth + node.data)
    for child in node.children:
    	indent_list(child, depth + 1)

def parse(s):
	# Given a string with nested parens, try to parse it!

	for i in range(len(s)):
		if s[i] == '(':
			print(s[i])
			# for j in range(len(s), i, -1):
			# 	if s[j] == ')':
			# 		ch = s[i:j+1]
			# 		print(ch)

# # Dynamic programming - fib sequence
# Notice that if we call, say, fib(5), we produce a call tree that calls the function on the same value many different times:

# fib(5)
# fib(4) + fib(3)
# (fib(3) + fib(2)) + (fib(2) + fib(1))
# ((fib(2) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + fib(1))
# (((fib(1) + fib(0)) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + fib(1))

# Instead of this, add a simple dict object, mapping each value already calculated to its result:
# This uses only O(n) but adds O(n) space

# MEMOIZATION!

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		pf = 0
		cf = 1
		for i in range(1, n):
			newf = pf + cf
			pf = cf
			cf = newf
	return cf









if __name__ == '__main__':
	# count_recursive()
	# print(lenlist([3, -2, 1, 9]))

	data = [1, [2, 3], 4]
	# print(doubler_flattener(data))
	# print(doubler_recursive(data))
	# print(doubler_no_loop(data))
	# print(parseRec(parseThis)) # Return the ans

	print(fib(5)) # 5
	print(fib(2)) # 1



