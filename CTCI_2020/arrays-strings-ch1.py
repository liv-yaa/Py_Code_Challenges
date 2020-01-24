# arrays-strings-ch1.py

"""
Interview Questions
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
Hints: #44, #117, #132
"""


# 1.2 - Done
def is_permutation(s1, s2):
	"""
	1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
	other.
	>>> is_permutation('sis', 'ssi')
	True
	>>> is_permutation('iss', 'ssi')
	True
	>>> is_permutation('', 'ssi')
	False
	>>> is_permutation('', '')
	True
	"""
	if s1 == s2:
		return True

	if s1 == '' or s2 == '':
		return False 

	cd1 = {i : s1.count(i) for i in s1}
	cd2 = {i : s2.count(i) for i in s2}

	return cd1 == cd2

# 1.3 - Not done
def urlify(s):
	"""
	URLify: Write a method to replace all spaces in a string with '%20'. IN PLACE

	>>> urlify('dlk 26')
	dlk%2026
	>>> urlify('Mr 3ohn Smit h 13')
	Mr%203ohn%20Smith

	"""
	return s.strip().replace(' ', '%20')


"""
1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tac t Coa
Output: Tru e (permutations : "tac o cat" , "atc o eta" , etc. )
Hints: #106, h 0134, § 136
"""
"""
1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale , pi e - > tru e
pales , pal e - > tru e
pale , bal e - > tru e
pale , bak e - > fals e
Hints: #23, #97, it 130
"""



# 1.6 - DONE
def string_compress(string):
	"""
	1.6 String Compression: Implement a method to perform basic string compression using the counts
	of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, 
	If the "compressed" string would not become smaller than the original string, your method 
	should return the original string. 
	You can assume the string has only uppercase and lowercase letters (a - z).

	>>> string_compress('')
	''
	>>> string_compress('eeeeeee')
	'7e'
	>>> string_compress('rroobbeerrttt')
	'2r2o2b2e2r3t'
	>>> string_compress('rroobbeerrt')
	'rroobbeerrt'
	>>> string_compress('oolivia')
	'oolivia'

	"""

	compressed = ''

	i = 0		
	curr = []       # Set up a set for the chunk

	if len(string) > 0:
		while i < len(string):
			curr.append(string[i]) # Get first item and add to set

			if len(set(curr)) > 1:
				chunk = curr[:-1]
				
				if len(chunk) > 1:
					compressed += str(len(chunk))
				compressed += chunk[0]
				
				del curr[:-1]
			
			i += 1

		if len(curr) > 1:
			compressed += str(len(curr))
		compressed += curr[0]

	if len(compressed) < len(string): 
		return compressed
	return string


def string_compress2(s):
	""" Better answer 
	>>> string_compress2('')
	''
	>>> string_compress2('eeeeeee')
	'7e'
	>>> string_compress2('rroobbeerrttt')
	'2r2o2b2e2r3t'
	>>> string_compress2('rroobbeerrt')
	'rroobbeerrt'
	>>> string_compress2('oolivia')
	'oolivia'


	"""
	compressed = []
	ct = 0

	for i in range(len(s)):
		if i != 0 and s[i] != s[i - 1]:
			compressed.append(str(ct) + s[i - 1])
			ct = 0
		ct += 1
	if s != '':
		compressed.append(str(ct) + s[-1])

	return min(s, ''.join(compressed), key=len)




# 1.7 - Done
def rotate_matrix(mat):
	"""
	Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
	bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

		first row of source ------> last column of destination
		second row of source ------> last but-one column of destination
		so ... on
		last row of source ------> first column of destination

	>>> rotate_matrix([[]]) # 1x1
	[[]]
	>>> rotate_matrix([[0, 0, 1, 1,], [0, 0, 1, 1], [3, 3, 2, 2], [3, 3, 2, 2]]) # 2 px by 2 px
	[[3, 3, 0, 0], [3, 3, 0, 0], [2, 2, 1, 1], [2, 2, 1, 1]]
	>>> rotate_matrix([[1, 2, 3], [0, 0, 0], [0, 0, 0]])
	[[0, 0, 1], [0, 0, 2], [0, 0, 3]]
	
	"""
	results = []
	n = len(mat)

	for i in range(n):
		innerArray = []
		for j in range(len(mat[i])):
			innerArray = [mat[j][i]] + innerArray
		results.append(innerArray)

	return results


# 1.8 - Done
def zero_matrix(mat):
	"""
	1.8 Zero Matrix: Write an algorithm such that if an element in an M x N matrix is 0, 
	its entire row and column are set to 0 in place. Hints: #17, #74, #102

	>>> zero_matrix([[0, 1, 1], [1, 1, 1]])
	[[0, 0, 0], [0, 1, 1]]
	>>> zero_matrix([[1, 1], [1, 1]])
	[[1, 1], [1, 1]]
	>>> zero_matrix([[1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
	[[0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [1, 0, 1, 1, 1]]
	>>> zero_matrix([[1, 0, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
	[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 0]]
	"""
	# keep track of the rows & cols that have zeroes:
	rows0 = set([i for i, row in enumerate(mat) if not all(row)])
	cols0 = set()
	for i in range(len(mat)): # rows
		for j in range(len(mat[i])): # cols
			elem = mat[i][j]
			if elem == 0:
				cols0.add(j)

	# Edit the entire column for all columns:
	for c in cols0:
		for i in range(len(mat)):
			mat[i][c] = 0

	# Edit the row for all rows:
	for r in rows0:
		mat[r] = [0] * len(mat[0])

	return mat

def zero_matrix2(mat):
	""" A few improvements:
		- Use 'in' or '~all' operator instead of iterating through each item
		- Use 'zip' to switch between rows and columns
		- Use comprehension, generators,
		- Make changes in place

	>>> zero_matrix2([[0, 1, 1], [1, 1, 1]])
	[[0, 0, 0], [0, 1, 1]]
	>>> zero_matrix2([[1, 1], [1, 1]])
	[[1, 1], [1, 1]]
	>>> zero_matrix2([[1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
	[[0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [1, 0, 1, 1, 1]]
	>>> zero_matrix2([[1, 0, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
	[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 0]]
	"""
	def locate_zero_rows(matrix: list) -> list:
		""" Given an NxM matrix, find rows that contain a zero """
		return [i for i, row in enumerate(matrix) if not all(row)]

	def locate_zero_cols(matrix: list) -> list:
		""" Given an NxM matrix, find cols that contain a zero 	
			zip() function for `parallel iteration`
				https://realpython.com/python-zip-function/
				Creates an iterator that aggregates elements from two or more iterables
				into tuples ex: zip([1, 1], [2, 2]) -> [(1, 2), (1, 2)]

		"""
		return locate_zero_rows(zip(*matrix)) # zips up the matrix the opposite way

	def zero_out(matrix):
		"""Given an NxM matrix zero out all rows and columns that contain at least one zero."""
		zero_rows = locate_zero_rows(matrix)
		zero_cols = locate_zero_cols(matrix)

		# print(zero_rows, zero_cols)

		for row in zero_rows:
			matrix[row] = [0] * len(matrix[0]) # num columns
		for col in zero_cols:
			for row in matrix:
				row[col] = 0

		return matrix

	return zero_out(mat)

# 1.9 - Done
def is_substring(sub, st):
	""" Checks if a string 'sub' is a permutation of string 'st'
		>>> is_substring('abs', 'crabs')
		True
		>>> is_substring('crabbs', 'abbs')
		True
		>>> is_substring('crabbs', 'basb')
		True
		>>> is_substring('', 'bruh')
		True
		>>> is_substring('xx', '')
		True
		>>> is_substring('ba', 'bruh')
		False
	>>> is_substring('sub', 'bus')
	True
	>>> is_substring('busses', 'sbs')
	True
	>>> is_substring('', 'bus')
	True
	>>> is_substring('sub', '')
	True
	>>> is_substring('sub', 'ccdb') # Characters are mutually exclusive 
	False
	>>> is_substring('subxxx', 'xccdb')
	False
	"""
	if len(sub) > len(st):
		return is_substring(st, sub)		# 'flipping'

	# Create a dict to store the counts of all characters in substring
	sub_dict = { c: sub.count(c) for c in sub }

	# Ensure that all characters in sub have the same or less frequency as their count in st.
	# Iterate through sub, and if any one freq is greater, return 'False' right away!
	for i in range(len(sub)):
		f_sub = sub_dict[sub[i]]
		f_st = st.count(sub[i])

		if f_sub > f_st:
			return False

	# return if no char counts are hi
	# An empty substring is also True
	return True

def is_substring_ordered(sub, st):
	""" Checks if a string 'sub' is an ordered substring of string 'st'
		>>> is_substring_ordered('abs', 'crabs')
		True
		>>> is_substring_ordered('crabbs', 'abbs')
		True
		>>> is_substring_ordered('crabbs', 'basb')
		False
		>>> is_substring_ordered('', 'bruh')
		True
		>>> is_substring_ordered('xx', '')
		True
		>>> is_substring_ordered('ba', 'bruh')
		False

	"""
	if len(st) < len(sub):
		return is_substring_ordered(st, sub)
	
	return sub in st

# 1.10 - Done
def string_rotation(s1, s2):
	"""
	1.9 String Rotation
	Assume you have a method is_substring which checks if one word is a substring of another. 
	Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
	call to  is_substring_ordered [e.g., "water bottle " is a rotation 'erbottlewat"),
	Hints: #34, #88,#W4 
	>>> string_rotation("ABCD", "CDAB") # rotate 1 right
	True
	>>> string_rotation("waterbottle", "waterbottle") # rotate 0
	True
	>>> string_rotation("waterbottle", "aterbottlew") # rotate 1 left
	True
	>>> string_rotation("waterbottle", "terbottlewa") # rotate 2 left
	True
	>>> string_rotation("waterbottle", "erbottlewat") # rotate 3 left
	True
	>>> string_rotation("waterbottle", "ewaterbottl") # rotate 1 right
	True
	>>> string_rotation("", "") # rotate 0
	True
	>>> string_rotation("b", "a")
	False
	>>> string_rotation("ba", "abb")
	False
	>>> string_rotation("banana", "ananb")
	False
	>>> string_rotation("ABCD", "ACBD")
	False
	"""
	# iterate through all rotations of s2 and see if they match s1:
	# print('s2', s2)
	if s1 == s2:
		return True
	
	for i in range(len(s2)):
		if s2[i + 1:] + s2[:i + 1] == s1:
			return True
	return False

def string_rotation2(s1, s2):

	"""
	An elegant answer - wow.
	>>> string_rotation2("ABCD", "CDAB") # rotate 1 right
	True
	>>> string_rotation2("waterbottle", "waterbottle") # rotate 0
	True
	>>> string_rotation2("waterbottle", "aterbottlew") # rotate 1 left
	True
	>>> string_rotation2("waterbottle", "terbottlewa") # rotate 2 left
	True
	>>> string_rotation2("waterbottle", "erbottlewat") # rotate 3 left
	True
	>>> string_rotation2("waterbottle", "ewaterbottl") # rotate 1 right
	True
	>>> string_rotation2("", "") # rotate 0
	True
	>>> string_rotation2("b", "a")
	False
	>>> string_rotation2("ba", "abb")
	False
	>>> string_rotation2("banana", "ananb")
	False
	>>> string_rotation2("ABCD", "ACBD")
	False
	"""
	if len(s1) != len(s2):
		return False

	temp = s1 + s1
	return temp.count(s2) > 0

if __name__ == "__main__":
	import doctest
	doctest.testmod()







































































































