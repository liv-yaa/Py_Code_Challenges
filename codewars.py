# codewars.py

# INTRO TO NUMPY 

from numpy import partition

def reorder(arr, n):
	"""
	numpy.partition() function is used to create a partitioned 
	copy of input array with its elements rearranged in such a 
	way that the value of the element in k-th position is in 
	the position it would be in a sorted array. 
	All elements smaller than the k-th element are moved before 
	this element and all equal or greater are moved behind it. 
	The ordering of the elements in the two partitions is undefined.
	"""
	return list(partition(arr, n))


def toJadenCase(string):
    return ' '.join([(word[0].upper() + word[1:]) for word in string.split(' ')])        
    