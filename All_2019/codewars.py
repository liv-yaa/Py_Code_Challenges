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


def solve(p):
    nSum(p)
    
def nSum(num):
    # If num is n-sum, it returns n 
    snum = str(num)
    print('num', num)
    
    for i in range(1, len(snum) + 1):
        # Get chunks of length i, starting from the end
        lst = []
        print('len', i)
        for j in range(len(snum) - i + 1):
            print('chunk', snum[j:j + i])
            lst.append(snum[j:j + i])
        print('lst', lst)


def toJadenCase(string):
    return ' '.join([(word[0].upper() + word[1:]) for word in string.split(' ')])        


for d in range(1, l + 1):
        print('d', d)
        # Get all chunks of length d or lower
        chx = [ snum[i:i + d] for i in range(0, l, d) ]
        print('chx', chx)


def generate_number(squad, n):
    # TODO: complete
    if n not in squad:
        return n

    # find any sums that add up to n
    for i in range(1, 10):
        for j in range(1, 10):
            if i + j == n:
                if int(str(i) + str(j)) not in squad:
                    return int(str(i) + str(j))
    return None


def upsidedown(x, y):
	# An upside down number is an integer that appears the same when rotated 180 degrees, as illustrated below.
    ns = [1, 2, 6, 8, 9, 0]
    up = [1, 5, 9, 8, 6, 0]
    for n in range(int(x), int(y) + 1):
        print(n)
        if all([d in ns for d in str(n)]):
        	print('n is true', n)
	        if n in ns:
	        	u = up[ns.idex(n)]
	        	print('u', u)







































