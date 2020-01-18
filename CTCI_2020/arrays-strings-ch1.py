# arrays-strings-ch1.py

"""
Interview Questions
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
Hints: #44, #117, #132
"""
"""
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
Hints: ft , #84, #122, #131
"""
"""
1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr 3ohn Smit h 13
Output: "Mr%203ohn%20Smith"
Hints: #53,0118
"""
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
"""
1.6 String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints: #92, if 110
"""
"""
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
Hints: «51,0100
"""
"""
1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
Hints: #17, #74, #102
"""

def is_substring(sub, st):
	""" Checks if a string 'sub' is a substring of string 'st'
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

	"""
	if len(sub) > len(st):
		# print('flipping')
		return is_substring(st, sub)

	# Create a dict to store the counts of all characters in substring
	sub_dict = { c: sub.count(c) for c in sub }
	# print(sub_dict)

	# Ensure that all characters in sub have the same or less frequency as their count in st.
	# Iterate through sub, and if the freq is bad, turn .
	for i in range(len(sub)):
		f_sub = sub_dict[sub[i]]
		f_st = st.count(sub[i])


		if f_sub > f_st:
			return False

	# return if no chars have been turned negative.
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

	



def string_rotation(s1, s2):
	"""
	1.9 String Rotation
	Assume you have a method is_substring which checks if one word is a substring of another. 
	Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
	call to isSubs t rin g [e.g., "wate r bottle " is a rotation oP'erbottlewat"),
	Hints: #34, #88,#W4 
	"""
	pass # Not done!



if __name__ == "__main__":
	import doctest
	doctest.testmod()







































































































