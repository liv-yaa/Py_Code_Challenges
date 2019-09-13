# Practce from edabit

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
		


def convert_to_hex(txt):
	"""
	>>> convert_to_hex("hello world")
	'68 65 6c 6c 6f 20 77 6f 72 6c 64'
	>>> convert_to_hex("Big Boi")
	'42 69 67 20 42 6f 69'
	>>> convert_to_hex("Marty Poppinson")
	'4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e'
	"""
	# return '4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e'




















if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print("All Tests Passed!")
