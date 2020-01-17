# https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm/solutions?solutionId=Dz9ML7J3d6FG85yw3

# LinkedListProblems

# Given the definition for a singly-linked list:

class ListNode(object):
	def __init__(self, x):
		self.value = x
		self.next = None

	def removeKFromList(l, k):
		c = l
		while c:
			if c.next and c.next.val == k:
				c.next = c.next.next
			else:
				c = c.next

		return l.next if l and l.value == k else l 