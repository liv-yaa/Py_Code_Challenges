# leetcodePracJan2020.py

def findOcurrences(text, first, second):
    """
    :type text: str
    :type first: str
    :type second: str
    :rtype: List[str]
    """
    s = text.split(" ")    
    return [s[i + 2] for i in range(len(s) - 2) if s[i] == first and s[i + 1] == second]
    
        
def gcdOfStrings(str1, str2):
	""" For there to be a common divisor between two strings str1 and str2, the shorter string str1 would be a prefix in the longer string str2 since the divisor T is repeated mulitiple times to form the string. """
	l1, l2 = len(str1), len(str2)

	if l2 > l1:
		# Ensures the longer string is str1 and the shorter or equal string is s2
		return gcdOfStrings(str2, str1)
	
	# See if str1 is a prefix of str2
	if str1[:l2] == str2:
		if l1 == l2:
			return str2
		else:
			return gcdOfStrings(str2, str1[l2:]) # Subtract the prefix

	return ''
    

def squareOfNWithBinarySearch(n):
	""" Calculates the square root of n using binary search """

	lo, hi = 0, x

	while lo <= hi:
		mid = (lo + hi) // 2

		if mid * mid > x:
			hi = mid - 1

		elif mid * mid < x:
			lo = mid + 1

		else:
			return mid

	return hi # There is no perfect square, so just return the val on the left


def heightChecker(heights):
	"""
	:type heights: List[int]
	:rtype: int # The number of students not standing in the right positions
	if they all want to stand in decreasing order
	"""
	return sum([1 for i in range(len(heights)) if heights[i] != sorted(heights)[i]])

def power3(n):
	"""  Check if n is a power of 3 """
	while (n % 3 == 0):
		n /= 3
	return n == 1

def power4(n):
	"""  Check if n is a power of 3 """
	while (n % 4  == 0):
		n /= 4
	return n == 1


if __name__ == "__main__":

	# print(findOcurrences("alice is a good girl she is a good student", "a", "good"))
	# print(gcdOfStrings("ABCABC", "ABC")) # "ABC"
	# print(gcdOfStrings("ABABAB", "ABAB")) # "AB"
	# print(gcdOfStrings("LEET", "CODE")) # ""
	print(power3(4), power3(144), power3(9), power3(81))
	print(power4(4), power4(144), power4(9), power4(81))


























































