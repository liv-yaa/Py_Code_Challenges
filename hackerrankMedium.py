# hackerrankMedium.py

import math
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
	all_magic_perms = [[list(p[:3]), list(p[3:6]), list(p[6:])] for p in permutations(range(1, 10)) if is_magic([p[:3], p[3:6], p[6:]])]

	# Iterate through all_magic_perms and get cost for s to be converted:
	# for perm in all_magic_perms:
	perm = all_magic_perms[0]
	cost = 0
	print('p', perm)
	print('s', s)

	for i in range(len(s)):
		for j in range(len(s)):

			if s == perm:
				print('success! cost :', cost)
				return cost

			# print(s[i][j], perm[i][j])

			cst = abs(s[i][j] - perm[i][j])
			print('cst', cst)

			if cst != 0:
				perm[i][j] = s[i][j]
				cost += cst
				print('cost updated, perm: ', perm)

	return cost



if __name__ == '__main__':
	s1 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
	print(formingMagicSquare(s1))

	# s2 = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
	# print(formingMagicSquare(s2))







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







