# hackerrankMedium.py

# import math
# import os
# import random
# import re
# import sys

def convertCost(matrix, const):
	""" Takes a matrix and returns the cost of converting it to the magic constant 
		If not possible, return None

	"""
	return 1



def formingMagicSquare(s):
	""" Def of MagicSquare:
		An  `n x n ` matrix of distinct positive integers from  to  where the sum of any row, column, 
		or diagonal of length  is always equal to the same number: the magic constant.
		You will be given a  matrix  of integers in the inclusive range [1-9]. 
		* We can convert any digit  to any other digit  in the range  at cost of |a-b|. 
		Convert it into a magic square at minimal cost. Print this cost on a new line.
	"""
	# Create a dict that takes the 
	cost_dict = {}

	for i in range(3, 28):
		cost_dict[i] = convertCost(s, i)

	return cost_dict


if __name__ == '__main__':
	s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
	print(formingMagicSquare(s))









    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







    







