# Dyanmic Programming examples https://www.geeksforgeeks.org/dynamic-programming/


def uglyNumbers(n):
	"""
	# **BRuTe WaY**
	Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
	[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
	Find the nth one

	>>> uglyNumbers(150)
	5832
	>>> uglyNumbers(15)
	24
	

	"""
	def maxDivide(a, b):
		""" Divides a by greatest divisible power of b """
		while a % b == 0:
			a = a / b
		return a

	def isUgly(no):
		""" Check if no is ugly or not - any of these"""
		no = maxDivide(no, 2)
		no = maxDivide(no, 3)
		no = maxDivide(no, 5)
		return 1 if no == 1 else 0

	i = 1
	count = 1
	while n > count:
		i += 1
		if isUgly(i):
			count += 1
	return i 


def uglyNumbers2(n):
	"""
	# **DynamiC WaY** - only uses O(n) extra space
	Ugly numbers are numbers whose only prime factors are 2, 3 or 5: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
	Find the nth one

	>>> uglyNumbers2(150)
	5832
	>>> uglyNumbers2(15)
	24

	Split into multiples of each :
	[2, 4, 6, 8, 10, 12, 14, 16, 18, ...]
	[3, 6, 9, 12, 15, 18, 21, 24, 27, ....]
	[5, 10, 15, 20, 25, 30, ...]

	Then do a merge sort - every step do smallest one
	
	"""
	ugly = [0] * n # to store all
	ugly[0] = 1 

	# Indexes for 2, 3, and 5:
	i2 = i3 = i5 = 0

	# Next multiple of each - set the value
	nxt2 = 2
	nxt3 = 3
	nxt5 = 5

	# Fill in `ugly`: Start loop to find value from ugly[1] to ugly[n]:
	for l in range(1, n):
		# Choose the min value of all available multiples:
		ugly[l] = min(nxt2, nxt3, nxt5)

		if ugly[l] == nxt2: #if we chose nxt2, it was min:
			i2 += 1			# Increment index of 2 to get the next multiple of 2 in the series
			nxt2 = ugly[i2] * 2 # update it to the next in the series

		if ugly[l] == nxt3:
			i3 += 1
			nxt3 = ugly[i3] * 3

		if ugly[l] == nxt5:
			i5 += 1
			nxt5 = ugly[i5] * 5

	# print(ugly)
	return ugly[-1]


def fibDynamic(n):
	"""

	Write a function int fib(int n) that returns Fn. For example, if n = 0, then fib() should return 0. If n = 1, then it should return 1. For n > 1, it should return Fn-1 + Fn-2
	>>> fibDynamic(9)
	34
	>>> fibDynamic(14)
	377

	Recusion for this would be exponential.
	How to solve with DP?
	- Store the fib numbers calculated so far

	"""
	fibArr = [0, 1]
	while len(fibArr) < n + 1:
		fibArr.append(0)
	
	if n <= 1:
		return n 

	else:
		# Recurse until you get to a 1.
		if fibArr[n - 1] == 0: # Start filling in the placeholder zeroes
			fibArr[n - 1] = fibDynamic(n - 1)

		if fibArr[n - 2] == 0:
			fibArr[n - 2] = fibDynamic(n - 2)

	# We got to 1! Now, time to sum up each layer of the recursion stack:
	fibArr[n] = fibArr[n - 2] + fibArr[n - 1]
	return fibArr[n]


def catalan(n):
	"""
	Count the number of expressions containing n pairs of parentheses which are correctly matched. 
	For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

	This follows a special `catalan` sequence: [1, 1, 2, 5, 14, 42, 132, ...]
	Recursive formula: catalan(n) is the sum of catalan(i) * catalan(n - i - 1)
	>>> catalan(1)
	1
	>>> catalan(3)
	5
	>>> catalan(4)
	14
	>>> catalan(8)
	1430

	"""
	if n <= 1:
		return 1

	res = 0
	for i in range(n):
		res += catalan(i) * catalan(n - i - 1)

	return res


def bellNumber(n):
	"""
	Given a set of n elements, find num of ways to partition it
	ex. given {1, 2}, it can be {{1, 2}} or {{1}, {2}}
	Let S(n, k) be total number of partitions of n elements into k sets. 

	>>> bellNumber(2)
	2
	>>> bellNumber(3)
	5
	"""

	bell = [[0 for i in range(n + 1)] for j in range(n + 1)]

	bell[0][0] = 1
	for i in range(1, n + 1):
		bell[i][0] = bell[i - 1][i - 1]

		for j in range(1, i + 1):
			bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]

	return bell[n][0]


def coinChange(coins, amount):
	""" 
	c = 1::
		i 
		1 	[0, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
		... becomes ....
		11  [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11] # The best number of `1` coins you need to make 0, 1, 2, .. 11

	c = 2::
		< skip 0 - 1 >
		
		i = 2: Success! Here, using a `2` coin for value 2 only counts 1 coin, 
		which is less than 2 from the previous round, so boot it out:
			[0, 1, 1, ......]
		i = 3: Success! here, using a `2` coin + `1` is better than 3x `1` coins
		i = 4: Success! here, using two `2` coins is better than four `1` coins
		i = 5: Success: .....
		i = 11: [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6] # The best we can do for each value only using `1` and `2` coins


	c = 5::
		< skip 0 - 4 >
		i = 5:
			Success! Here, using one `5` coin is better than three smaller coins
		i = 6, ... all success
		i = 11: [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]




	>>> coinChange([1, 2, 5], 11)
	3
	>>> coinChange([2], 3)
	-1
	"""

	if not amount: return 0
	min_coins = [0] + [float('inf')] * amount

	# Iterate through all coin values
	for c in coins:
		# Iterate through amounts it could be (dont waste time with amounts 0 < c)
		for i in range(c, amount + 1):
			# Check if adding a new coin minimizes the previous value
			min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)

	return min_coins[-1] if min_coins[-1] != float('inf') else -1


def coinChange2(n):
	"""
	Uses a table instead, Construct table in a bottom up manner:

	>>> coinChange2(4)
	4
	"""
	coins = [1, 2, 3] # Coin types

	table = [0 for k in range(n + 1)] # table[i] Will be storing the number of solutions for value i
	table[0] = 1 # base case

	# Pick all coins one by one and update all vals 
	# after that index to reflect how we add this new coin type
	for c in coins:
		for j in range(c, n + 1):
			table[j] = table[j] - table[j - c]


def rotOranges(p, q, r, s):
	"""
	Calc the time it takes to rot all oranges
	@args matrix m * n where cells in matrix have 0, 1, 2
	A rotten orange at index [i, j] can rot other fresh oranges at indexes [i – 1, j], [i + 1, j], [i, j – 1], [i, j + 1] (up, down, left and right). 

	"""

	
























# def parenthesesProb(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    

