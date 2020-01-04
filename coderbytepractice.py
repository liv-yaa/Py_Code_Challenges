# coderbyte practice

def LetterChanges(str):
	""" Have the function LetterChanges(str) take the str parameter being passed and modify it using 
	the following algorithm. Replace every letter in the string with the letter following it in the alphabet 
	(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and 
	finally return this modified string.Have the function LetterChanges(str) take the str parameter being 
	passed and modify it using the following algorithm. Replace every letter in the string with the letter 
	following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string
	 (a, e, i, o, u) and finally return this modified string. """
	out = ''
	for let in str:
		if ord(let) == 90:
			out += 'A'
		elif ord(let) == 122:
			out += 'a'
		elif (64 < ord(let) and ord(let) < 90) or (96 < ord(let) and ord(let) < 122) :
			out += chr(ord(let) + 1)
		else:
			out += let

	out = out.replace('a', 'A').replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U')
	return out

def betterLetterChanges(st):
	letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW"
	changes = "bcdEfghIjklmnOpqrstUvwxyzABCDEFGHIJKLMNOPQRSTUVWZ"
	mapping = { k:v for (k, v) in zip(st + letters, st + changes)}
	return ''.join([ mapping[c] for c in st ])


def SimpleAdding(num): 
	"""
	Have the function SimpleAdding(num) add up all the numbers from 1 to num. For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10. For the test cases, the parameter num will be any number from 1 to 1000.
	num <= 1000.
	"""
	return sum([n for n in range(1, num + 1)])


def twoSum(arr, S):
	""" 
	https://coderbyte.com/algorithm/two-sum-problem
	Find all pairs of two integers in unsorted array that add up to S 
	* Dont loop twce - O(n^ 2)
	* better - try to get O(n) time
		* Use Hash Tables / Dictionary with constant lookup time
	"""
	sums = []
	hAsh = {}

	for a in arr:
		# Check if x = S - a exists in the hash table
		if S - a in hAsh:
			sums.append((a, S - a))

		# Add a to the hash table
		hAsh[a] = a

	return sums 	


def powerSet(arr):
	""" The power set contains every possible combination of numbers. It also includes the empty set which contains no numbers from the original set.
		There will be 2 ^ N possible combinations of this set 
		Every element can either be in the set or not, so 2 * 2 * 2...=2 ^ N
	
	Algorithm:
		1. Loop through 0 to 2 ^ N
		2. Convert to binary
		3. Use the binary to exclude (0) or include (1)

	Run Time:
		Best case is O(2^n) time which is very slow. But this is the best worst case.
	"""
	pS = []
	for i in range(2 ** len(arr)):
		bi = format(i, '#05b')[2:]
		pS.append([arr[j] for j in range(3) if bi[j] == '1'])

	return pS


def patterns(st, al=[]):
	""" 
	https://coderbyte.com/algorithm/find-all-string-combinations-consisting-zero-one-wildcard
	Print all possible combinations of a string of 0 & 1, where ? is a wildcard that is either 0 or 1
	
	Algo:
		1. Call the fxn w/ the string & an empty set where we begin bushing 0's and 1's
		2. Once we reach a ?, make a copy of each string set
			for half append a 0, other half append a 1
		3. Recursively call the function on smaller strings. Base case = break when string is empty

	"""

	# print('al', al, 'st', st)

	if len(st) == 0: # base case
		return al

	if st[0] == '0' or st[0] == '1':
		# Add the character to each string we have so far
		for i in range(len(al)):
			al[i] = al[i] + [int(st[0])]
		# print('al', al)


	if st[0] == '?':
		# For a wildcard, make a copy of each string set
		# For half of them append a 0 to the string, other half append 1 
		# print('?')

		# Get the first char from each item in al:
		for j in range(len(al)):
			temp = al[j][::]
			# print('temp', temp)
			al.append(temp)

		# print('al', al)

		for k in range(len(al)):
			if k < len(al) / 2:
				al[k].append(0)
			else:
				al[k].append(1)
		# print('al now', al)

	return patterns(st[1:], al)




if __name__ == "__main__":
	""" if this were a module, use this format """
	# print(twoSum([3, 5, 2, -4, 8, 11], 7))
	# print(powerSet([1, 2, 3]))
	print(patterns('?10??', [[1, 0], [0, 1]]))
























