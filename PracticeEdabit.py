# Practce from edabit 9-13-2019
# For 

def count_boomerangs(arr):
	"""
	https://edabit.com/challenge/25zkiePFYRpickxn
	A boomerang is a V-shaped sequence that is either upright or upside down. Specifically, a boomerang can be defined as: sub-list of length 3, with the first and last digits being the same and the middle digit being different.
	returns the total number of boomerangs in a list.
	>>> count_boomerangs([9, 5, 9, 5, 1, 1, 1])
	2
	>>> count_boomerangs([5, 6, 6, 7, 6, 3, 9])
	1
	>>> count_boomerangs([4, 4, 4, 9, 9, 9, 9])
	0
	"""

	count = 0

	if len(arr) >= 3:

		for i in range(len(arr) - 2):

			if arr[i] == arr[i + 2] and (arr[i + 1] != arr[i + 2]) and (arr[i + 1] != arr[i]):
				count += 1

	# print(count)
	return count


def first_before_second(string, l1, l2):
	"""
	Write a function that returns True if every instance of the first letter l1 occurs before every instance of the second letter l2.
	>>> first_before_second("a rabbit jumps joyfully", "a", "j")
	True
	>>> first_before_second("knaves knew about waterfalls", "k", "w")
	True
	>>> first_before_second("precarious kangaroos", "k", "a")
	False

	"""
	# if we find l1, keep going
	# if we find l2, and then find l1, return False
	# if we find l2, and never find l1, return True
	foundL2 = False

	for i in range(len(string)):
		if string[i] == l2:
			# print(i, l2)
			foundL2 = True

		if string[i] == l1 and foundL2 == True:
			return False

	return True
		

# def convert_to_hex(txt):
	"""
	>>> convert_to_hex("hello world")
	'68 65 6c 6c 6f 20 77 6f 72 6c 64'
	>>> convert_to_hex("Big Boi")
	'42 69 67 20 42 6f 69'
	>>> convert_to_hex("Marty Poppinson")
	'4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e'
	"""
	# return '4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e'

	# out = ""

	# for char in txt:
	# 	# print(char)

	# 	if char != ' ':

	# 		out += str(ord(char)) + ' '

	# return out


def matrixElementsSum(matrix):

    # Method: add up the sum. Haunted are 0 so it doesn't matter.
    # Next, subtract the rooms directly below the haunted ones
        
    s = 0
    haunted = list()
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):            
            if matrix[i][j] == 0:
                haunted.append(tuple((i, j)))
            s += matrix[i][j]
                
    print(haunted)
    
        
    

            

    print(s)


def allLongestStrings(inputArray):
    # return Array of the longest strings, stored in the same order
    
    ml = max([len(item) for item in inputArray])    
    out = [item for item in inputArray if len(item) == ml]

    return out


def commonCharacterCount(s1, s2):
    # "common" means the minimum count of characters, if they overlap
    
    common = set()
    total = 0
    
    for l in s1:
        if l in s2 and l not in common:
            # get min
            common.add(l)
            total += min(s1.count(l), s2.count(l))

    return total


def isLucky(n):
    # A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
    # Has even number of digits
    
    sum1 = sum([int(i) for i in str(n)[ : len(str(n)) // 2]])
    sum2 = sum([int(i) for i in str(n)[len(str(n)) // 2 : ]])
            
    return sum1 == sum2


def advanced_sort(lst):
	""" Create a function that takes a list of numbers or strings and returns a 
	list with the items from the original list stored into sublists. 
	Items of the same value should be in the same sublist.
	>>> advanced_sort([2, 1, 2, 1])
	[[2, 2], [1, 1]]
	>>> advanced_sort([5, 4, 5, 5, 4, 3])
	[[5, 5, 5], [4, 4], [3]]
	>>> advanced_sort(["b", "a", "b", "a", "c"])
	[['b', 'b'], ['a', 'a'], ['c']]
	
	# Works:
	outlist = []
	for item in set(lst):
		outlist.append([item] * (lst.count(item)))
		
		print(outlist)

	return(outlist)


	"""

	outlist = []
	passed = []

	for item in lst:
		if item not in passed:
			outlist.append([item] * (lst.count(item)))
			passed.append(item)

	return(outlist)


def is_prim_pyth_triple(lst):
	""" 
	Return if a^2 + b^2 = c^2 is true
	AND
	the greatest common prime factor between any two numbers is 1.

	>>> is_prim_pyth_triple([4, 5, 3])
	True
	>>> is_prim_pyth_triple([7, 12, 13])
	False
	>>> is_prim_pyth_triple([39, 15, 36])
	False
	>>> is_prim_pyth_triple([77, 36, 85])
	True

	"""
	l = sorted(lst)
	a, b, c = l[0], l[1], l[2]

	# Find GCP of all three numbers
	a_factors = [i for i in range(1, a + 1) if a % i == 0]
	b_factors = [i for i in range(1, b + 1) if b % i == 0]
	c_factors = [i for i in range(1, c + 1) if c % i == 0]


	common = [i for i in range(1, c + 1) if (i in a_factors) and (i in b_factors) and (i in c_factors)]

	return (a**2 + b**2 == c**2) and (common == [1])



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print("All Tests Passed!")
