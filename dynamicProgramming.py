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
	# print(fibArr)
	
	if n <= 1:
		return n 

	else:
		if fibArr[n - 1] == 0:
			fibArr[n - 1] = fibDynamic(n - 1)

		if fibArr[n - 2] == 0:
			fibArr[n - 2] = fibDynamic(n - 2)

	fibArr[n] = fibArr[n - 2] + fibArr[n - 1]
	return fibArr[n]
































if __name__ == "__main__":
    import doctest
    doctest.testmod()
    

