# hackerrankMedium.py

# import math
# import os
# import random
# import re
# import sys
from itertools import permutations

def is_magic(mat):
	""" Determines if a linear list representing a matrix `mat` is magic 
		Rows, columns, and diagonals
	"""
	rs = set([sum(mat[i]) for i in range(3)])
	cs = set([sum([mat[j][i] for j in range(3)]) for i in range(3)])
	ds = set([sum([mat[0][0], mat[1][1], mat[2][2]]), sum([mat[0][2], mat[1][1], mat[2][0]])])

	# print(rs, cs, ds)    /s

	return len(rs) == 1 and len(cs) == 1 and len(ds) == 1

def formingMagicSquare(s):
	""" Def of MagicSquare:
		An  `n x n ` matrix of distinct positive integers from  to  where the sum of any row, column, 
		or diagonal of length  is always equal to the same number: the magic constant.
		You will be given a  matrix  of integers in the inclusive range [1-9]. 
		* We can convert any digit  to any other digit  in the range  at cost of |a-b|. 
		Convert it into a magic square at minimal cost. Print this cost on a new line.


		Algo:
			1. Find all possible 3x3 magic square
			2. Compute cost of changing s into a known magic square
	"""

	# There are 8 magic squares - check all permutations of [1-9]


	# print(s, is_magic(s))

	all_magic_perms = []

	for p in permutations(range(1, 10)):
		lp = list(p)
		mp = [lp[:3], lp[3:6], lp[6:]]

		if is_magic(mp):
			print(mp)

	return all_magic_perms





if __name__ == '__main__':
	s1 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
	formingMagicSquare(s1)

	s2 = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
	# print(formingMagicSquare(s2))







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







