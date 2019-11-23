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






def hammingDistance(self, x: int, y: int) -> int:
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



























