# leetcode practice

def twoSum(nums, target):
	# Total O(n)
	d = {}
	for i in range(len(nums)): # O(n)
		ch = target - nums[i]
		if ch in d: # Lookup in dict is O(1)
			return (d[ch], i)
		d[nums[i]] = i 

	return []

from itertools import *
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # Time limit exceeded
    un = []
    for c in combinations(nums, 3):
        if sum(c) == 0 and sorted(c) not in un:
            un.append(sorted(c))
    return un
            

#time limit exceeded
def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """ 
    # sell price must be larger than buy price
    
    if not prices:
    	return 0
 
	mn = max(prices) # initialize min price
	pt = 0 # initialize max profit

	for p in prices:
		mn = min(mn, p)
		pt = max(pt, p - mn) # update profit if it's bigger

	return pt 


def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

# output exceeded
def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output = []
        for i in range(len(nums)):
            n = 1
            for j in range(len(nums)):
                if i != j:
                    n = n * nums[j]
            output.append(n)

        return output


# Initiate an array of size amount + 1 to store the minimum number of coins that make up each amount possible from 0 to the required amount. The first value is initiated as 0 so that new values can be added (see code), the rest N are set to float('inf').
# Iterate through coin values first and through amounts in the nested loop. This is so to not waste time going through amounts 0, 1, ..., (i + 1) which the selected coin cannot contribute to. E.g. for coin of value 2, there's no need to check if it can contribute to the minimum number of coins to sum up 0 or 1.
# Compute the minimum number of coins for each amount and check if adding a new coin minimizes the previous value.
def coinChange(coins: List[int], amount: int) -> int:
	if not amount:
		return 0

	min_coins = [0] + [float('inf')] * amount

	for c in coins:
		for i in range(c, amount + 1):
			min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)

		return min_coins[-1] if min_coins[-1] != float('inf') else -1


def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        return str(x) == str(x)[::-1]


def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """        
        
        rc, lc, res = 0,0,0
        
        for let in s:
            if let == 'R':
                rc += 1
            else:
                lc += 1
                
            if rc == lc:
                res += 1
                rc, lc = 0,0
                
        return res





# Write your MySQL query statement below
SELECT name, population, area 
    FROM World
        WHERE area > 3000000 or population > 25000000;




    
def selfDividingNumbers(self, left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    
    Runtime: O(m) * O(n) where m is range(left,right) and n is range(len(m))
    """
    return [m for m in range(left, right + 1) if '0' not in str(m) and all([m % int(d) == 0 for d in str(m)])]


def hammingDistance(self, x, y):
	return sum([c=='1' for c in bin(x^y)[2:]])


def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        return ''.join([c for c in S if c not in 'aeiou'])


def defangIPaddr(self, address):
    """
    :type address: str
    :rtype: str
    """
    
    return address.replace('.', '[.]')


def calculateTime(self, kb, word):
        """
        :type kb: str
        :type word: str
        :rtype: int
        """
        time = kb.index(word[0])
        
        for i in range(len(word) - 1):
            x = kb.index(word[i])
            y = kb.index(word[i + 1])
            time += abs(x - y)
            
        return time


def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        return [B.index(it) for it in A]


def uniqueOccurrences(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    x = [arr.count(n) for n in set(arr)]
    return len(x) == len(set(x))


def fixedPoint(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    i = 0
    while i < len(A):
        if A[i] == i:
            return i
        i += 1
    return -1


def peakIndexInMountainArray(self, A):
    """
    :type A: List[int]
    :rtype: int
    
    "Given that it is definetly a mountin...return the peak"
    """
    
    for i in range(len(A)):
        if A[i] > A[i + 1]:
            return i


def highFive(self, items):
    """
    :type items: List[List[int]]
    :rtype: List[List[int]]
    """
    sdic = {}
    for i in range(len(items)):
        sid = items[i][0]
        sco = items[i][1]
        
        if sid not in sdic:
            sdic[sid] = [sco]
            
        else:
            c = sdic[sid]
            c.append(sco)
            sdic[sid] = c
                
    avs = []
    for i in sdic:
        av = sum(sorted(sdic[i])[-5:]) // 5            
        avs.append([i, av])
                
    return avs
        

def sumOfDigits(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    
    if sum([int(d) for d in str(min(A))]) % 2 == 1:
        return 0
    return 1


def isArmstrong(self, N):
    """
    :type N: int
    :rtype: bool
    """     
    return N == sum([int(d) ** len(str(N)) for d in str(N)])
        
        
def lastStoneWeight(self, stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    while True:
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones[0]
        else:
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            if abs(x - y) != 0:
                stones.append(abs(x - y))


def findWords(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    okk = []
    
    for w in words:
        o1 = [l for l in w if l.upper() in 'QWERTYUIOP']
        o2 = [l for l in w if l.upper() in 'AASDFGHJKL']
        o3 = [l for l in w if l.upper() in 'ZXCVBNM']
        
        if len(o1) == len(w) or len(o2) == len(w) or len(o3) == len(w):
            okk.append(w)
              
    return okk


def sumEvenAfterQueries(self, A, queries):
    """
    Output limit exceeded
    :type A: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    out = []
    for q in queries:
        A[q[1]] = A[q[1]] + q[0]            
        evens = [e for e in A if e % 2 == 0]
        out.append(sum(evens))
        
    return out


def sumEvenAfterQueries(self, A, queries):

	""" Looked up answer
    :type A: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """

    out = []
    sumNum = sum(map(lambda x : x if x % 2 == 0 else 0, A))

    for i in queries:
    	prv = A[i[1]]
    	aft = A[i[1] + i[0]]

    	if prv % 2 == 0 and aft % 2 == 0:
    		sumNum = sumNum + i[0]

		elif prv % 2 == 0 and aft % 2 != 0:
			sumNum = sumNum - prv 

		elif prv % 2 != 0 and aft % 2 == 0:
			sumNum = sumNum + aft

		else:
			pass

		out.append(sumNum)
		A[i[1]] = A[i[1] + i[0]]

	return out


def heightChecker(self, heights: List[int]) -> int:
	ctr = 0
	for i, j in zip(heights, sorted(heights)):
		if (i != j):
			ctr += 1

	return ctr


def largestUniqueNumber(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    
    out = [n for n in A if A.count(n) == 1]

    if out != []:
        return max(out)
    else:
        return -1


def minimumAbsDifference(self, arr):
    """
    Time Limit Exceeded

    :type arr: List[int]
    :rtype: List[List[int]]
    """
    out = []
    mad = 1000000 # minimum absolute difference
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if abs(arr[i] - arr[j]) < mad:
                    mad = abs(arr[i] - arr[j])        
    for a in arr:
        for b in arr:
            if a < b and (b - a) == mad:
                out.append((a, b))
                
    return sorted(out)


def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
	arr.sort()                                            # arrange-the array to make it easier to iterate
	k = min(j-i for i,j in zip(arr,arr[1:]))              # find the minumum to compare
	return [[i,j] for i,j in zip(arr,arr[1:]) if j-i ==k] # obtain result using one listComprehension


def numRookCaptures(self, board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                
                # Try to go S:
                x, y = i, j
                while x <= 8:
                    x += 1
                    if  x == 8:
                        break
                    elif board[x][y] == 'B':
                        break
                    elif board[x][y] == 'p':
                        count += 1
                        break
                        
                # Try to go N:
                x, y = i, j 
                while x >= -1:
                    x -= 1
                    if x == -1:
                        break
                    elif board[x][y] == 'B':
                        break
                    elif board[x][y] == 'p':
                        count += 1
                        break
                        
                # Try to go E:
                x, y = i, j 
                while y <= 8:
                    print(x, y, board[x][y])
                    y += 1
                    if y == 8:
                        break
                    elif board[x][y] == 'B':
                        break
                    elif board[x][y] == 'p':
                        count += 1
                        break
                    
                    
                # Try to go W:
                x, y = i, j 
                while y >= -1:
                    print(x, y, board[x][y])
                    y -= 1
                    if y == -1:
                        break
                    elif board[x][y] == 'B':
                        break
                    elif board[x][y] == 'p':
                        count += 1
                        break
                    
    return count
            

def canThreePartsEqualSum(self, A):
    """
    Time limit exceeded

    :type A: List[int]
    :rtype: bool
    Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.
    
    """
    for i in range(len(A)):
        for j in range(len(A)):
            if sum(A[:i+1]) == sum(A[i+1:j]) == sum(A[j:len(A)]):
                # print(sum(A[:i+1]), sum(A[i+1:j]), sum(A[j:len(A)]))
                # print(i, j)
                if len(A[:i+1]) != 0 and len(A[i+1:j]) != 0 and len(A[j:len(A)]) != 0:
                    return True
            
    return False



def canThreePartsEqualSum(self, A: List[int]) -> bool:
    if sum(A) % 3 != 0: return False
    res = sum(A) // 3
    count = 0
    sign = 0
    for i in range(len(A)):
        count += A[i]
        if count == res:
            sign += 1
            if sign == 3:
                return True
            count = 0
    return False





def uncommonFromSentences(self, A, B):
    """
    :type A: str
    :type B: str
    :rtype: List[str]
    A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence. Return a list of all uncommon words. 
    """
    
    c = A.split(" ") + B.split(' ')
    return [w for w in c if c.count(w) == 1]


def isMajorityElement(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    
    if target is an element that appears more than N/2 times in an array of length N.
    """
    
    return nums.count(target) > len(nums) / 2

































