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


def canPermutePalin(s):
	counts = {}
	for c in s:
		if c not in counts:
			counts[c] = 1
		else:
			counts[c] += 1
	print("counts = ", counts)

	flag_odd = False

	for k, v in counts.items():
		print(k, v)

		if (v % 2 == 1):
			if (flag_odd == True):
				return False
			flag_odd = True
	return True


def canPermutePalindrome(self, s: str) -> bool:
    counts = {}
    for c in s:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    # print("counts = ", counts)

    flag_odd = False

    for k, v in counts.items():
        # print("k = ", k, " v = ", v)

        if (v % 2 == 1):
            if (flag_odd == True):
                return False
            flag_odd = True
    return True


def similarRGB(self, color):
    """
    :type color: str
    :rtype: str

    ROunding by component - i dont understand
    """

    def f(comp):
    	q, r = divmod(int(comp, 16), 17)
    	if r > 8:
    		q += 1
		return '{:02x}'.format(17 * q)

	return '#' + f(color[1:3]) + f(color[3:5]) + f(color[5:])


def averageOfLevels(self, root: TreeNode) -> List[float]:
    def level(root, l, depth):
        if root:
            if len(l) <= depth:
                l.append([])
            l[depth].append(root.val)
            level(root.left, l, depth+1)
            level(root.right, l, depth+1)
    s = []
    level(root, s, 0)
    return [sum(i)/len(i) for i in s]


def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    
    out = ''
    if num >= 1000:
        b4 = int(str(num)[-4])
        print('b4', b4)

        out += 'M' * b4
        
    
    if num >= 100:
        b3 = int(str(num)[-3])
        print('b3', b3)
        if b3 < 4:
            out += 'C' * b3
        elif b3 == 4:
            out += 'CD'
        elif 4 < b3 < 9:
            out += 'D' + 'C' * (b3 - 5)
        elif b3 == 9:
            out += 'CM'
            
            
    if num >= 10:
        b2 = int(str(num)[-2])
        print('b2', b2)
        if b2 < 4:
            out += 'X' * b2
        elif b2 == 4:
            out += 'XL'
        elif 4 < b2 < 9:
            out += 'L' + 'X' * (b2 - 5)
        elif b2 == 9:
            out += 'XC'
    
    # get ones place
    b1 = int(str(num)[-1])
    print('b1', b1)

    # Dont have to handle 0 case
    if b1 < 4:
        out += 'I' * b1
    elif b1 == 4:
        out += 'IV'
    elif 4 < b1 < 9:
        out += 'V' + 'I' * (b1 - 5)
    elif b1 == 9:
        out += 'IX'
    
    
    return out


class HitCounter(object):
    """
    # Your HitCounter object will be instantiated and called as such:
    # obj = HitCounter()
    # obj.hit(timestamp)
    # param_2 = obj.getHits(timestamp)
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeHits = {0: 0} # Timestamp : total hits at that time stamp
        

    def hit(self, ts):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """        
        # Increment dictionary
        if ts in self.timeHits:
            self.timeHits[ts] = self.timeHits[ts] + 1
        else:
            self.timeHits[ts] = 1
        

    def getHits(self, ts):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """        
        total = 0
        for k, v in self.timeHits.items():
            if ts - 300 < k <= ts:
                total += v
                
        return total


def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    """
    p = 0
    while not all([n == 0 for n in nums[len(nums) - nums.count(0):]]):
        if nums[p] == 0:
            nums.append(nums.pop(p))
        elif nums[p] != 0:
            p += 1
                        
    return nums        


def firstUniqChar(self, s: str) -> int:
    """Returns the index of first non-repeating char, give a string.
    
    Input
    s: str
    
    Output
    int
    """
    if not s:
        return -1
    
    hashmap = Counter(s)

    for index, char in enumerate(s):
        if hashmap[char] == 1:
            return index
    return -1


def climbStairs(self, n):
    """
    Time limit exceeded
    :type n: int
    :rtype: int
    You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """
    if n <= 1:
        return 1
    else:
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    pass
    """
    ways = [1, 1]
    for i in range(2, n + 1):
        ways.append(ways[-1] + ways[-2])
                    
    return ways[-1]



def validPalindrome(self, s):
    """
    Time Limt Ex
    :type s: str
    :rtype: bool
    """
    
    if s == s[::-1]:
        return True
    
    for i in range(len(s)):
        t = s[:i] + s[i + 1:]
        # print(t)
        if t == t[::-1]:
            return True
    
    return False






def validPalindrome(self, s: str) -> bool:
    l, r = 0, len(s)-1
    def isPalin(s):
        return s==s[::-1] 
    while l<r:
        if s[l]!=s[r]:
            return isPalin(s[l+1:r+1]) or isPalin(s[l:r])
        l += 1
        r -= 1
    return True


def isRectangleOverlap(recA, recB):
    """
    :type rec1: List[int]
    :type rec2: List[int]
    :rtype: bool
    Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap. Given two (axis-aligned) rectangles, return whether they overlap.
    """
    
    x1a, y1a, x2a, y2a = recA[0], recA[1], recA[2], recA[3]
    x1b, y1b, x2b, y2b = recB[0], recB[1], recB[2], recB[3]
    return (x2a - x1b > 0) and (y2a - y1b > 0) and (x1a - x2b < 0) and (y1a - y2b < 0)


class MyHashMap(object):
    """
    I used a dict which was not in the specs
    # Your MyHashMap object will be instantiated and called as such:
    # obj = MyHashMap()
    # obj.put(key,value)
    # param_2 = obj.get(key)
    # obj.remove(key)
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashmap[key] = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        
        if key in self.hashmap:
            return self.hashmap[key]
        else:
            return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key in self.hashmap:
            del self.hashmap[key]


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class AnsHashMap:
    def __init__(self):
        self.size = 1000
        self.hash_table = [None] * self.size

    def put(self, key:int, value: int) -> None:
        index = key % self.size

        if self.hash_table[index] == None:
            self.hash_table[index] = ListNode(key, value)
        else:
            curr_node = self.hash_table[index]
            while True:
                if curr_node.key == key:
                    curr_node.value = value
                    return
                if curr_node.next == None:
                    break 
                curr_node = curr_node.next

            curr_node.next = ListNode(key, value)


    def get(self, key: int) -> int:
        if self.hash_table[index] == None:
            self.hash_table[index] = ListNode(key, value)


def parens(s):
    stack = []

    for c in s:
        if c == '(':
            stack.append(0)
        elif c == ')':
            if len(stack) > 0 and stack[-1] == 0:
                stack.pop()
            else:
                return False

    if stack == []:
        return True
    else:
        return False


def parens2(s):
    stack = []

    for c in s:
        if c =='(':
            stack.append(0)
        elif c == ')':
            if len(stack) > 0 and stack[-1] == 0:
                stack.pop()
            else:
                return False

    if stack == []:
        return True 
    else:
        return False


def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int):
    # https://leetcode.com/problems/flood-fill/discuss/444695/Readable-Python

    def check_color(self, r, c):
        if self.valid_pixel(r, c) and self.m[r][c] == self.old:
            self.m[r][c] = self.new
            self.stack.append((r, c))

    def valid_pixel(self, r, c):
        if (0 <= r <= self.r_max) and (0 <= c <= self.c_max):
            return True
        return False

    if not image or not image[0] or newColor == image[sr][sc]:
        return image

    self.c_max = len(image[0]) - 1
    self.r_max = len(image) - 1

    self.m = image
    self.old = self.m[sr][sc]
    self.new = newColor
    self.m[sr][sc] = self.new
    self.stack = [(sr, sc)]
    while self.stack:
        r, c = self.stack.pop()
        up = (r - 1, c)
        dn = (r + 1, c)
        lf = (r, c - 1)
        ri = (r, c + 1)

        for direction in [up, dn, lf, ri]:
            self.check_color(*direction)

    return self.m


def getKey(my_dict, value):
    # Gets a key from the value

    # kl = list(my_dict.keys())
    # vl = list(my_dict.values())

    # return kl[vl.index(value)]

    for k, v in my_dict.items():
        if v == value:
            return k

    return None



def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    inter = []
    
    for n in nums1:
        if n in nums2:
            if n not in inter:
                inter.append(n)
    for n in nums2:
        if n in nums1:
            if n not in inter:
                inter.append(n)
            
    return inter




def findShortestSubArray(self, nums):
    if nums == []:
        return 0
    dic = {}
    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1

    degree = max(dic.values())
    if degree == 1:
        return 1
    else:
        min_length = len(nums)
        for keys in dic:
            if dic[keys] == degree:
                pos1 = nums.index(keys)
                pos2 = len(nums) - nums[::-1].index(keys) - 1
                if pos2 - pos1 + 1 < min_length:
                    min_length = pos2 - pos1 + 1
    return min_length


    """ Looked up answer
    :type A: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """

    return_list = []
    sum_num = sum(map(lambda x : x if x%2==0 else 0,A))
    for i in queries: 
        prv = A[i[1]]

        after = A[i[1]]+i[0]

        if prv%2 == 0 and after%2 == 0:
            sum_num = sum_num+i[0]

        elif prv%2 == 0 and after%2 != 0:
            sum_num = sum_num - prv

        elif prv%2 != 0 and after%2 == 0:
            sum_num = sum_num+after

        else:
            pass
        return_list.append(sum_num)
        A[i[1]] = A[i[1]]+i[0]

    return return_list

def singleNumber(self, nums):
    """
    Find the one number that does not appear twice
    * Uses a stack * 
    """
    single = []
    for n in nums:
        if n not in single:
            single.append(n)
        else:
            single.remove(n)
    return single[0]


#Doing these: https://medium.com/better-programming/the-software-engineering-study-guide-for-interviews-53b42d82deb0
def fizzBuzz(m):
    for n in range(1, m + 1):
        if n % 15 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)


def subarraySum(nums, k):
    prefix_dict = {0:1}
    cur_sum = 0
    res = 0

    for n in nums:
        cur_sum += n
        lookfor = cur_sum - k

        if lookfor in prefix_dict:
            res += prefix_dict[lookfor]

        if cur_sum not in prefix_dict:
            prefix_dict[cur_sum] = 1

        else:
            prefix_dict[cur_sum] += 1


def BADsumEvenAfterQueries(self, A, queries):

        """ Looked up answer
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        out = []
        for i in range(len(queries)):
            if queries[i][1] < len(A):
                A[queries[i][1]] = A[queries[i][1]] + queries[i][0]
            out.append(sum([e for e in A if e % 2 == 0]))
                
        return out


def sumEvenAfterQueries(self, A, queries):
    eve = sum([A[i] for i in range(len(A)) if A[i] % 2 == 0])
    m = []

    for i in range(len(queries)):
        if (A[queries[i][1]] % 2 == 0):

            if (A[queries[i][0]] % 2 == 0):
                eve += queries[i][0]
            else:
                eve -= A[queries[i][1]]
            A[queries[i][1]] += queries[i][0]
        else:
            if (queries[i][0] % 2 == 0):
                eve = eve  
            else:
                eve += (A[queries[i][1]] + queries[i][0])
            A[queries[i][1] += queries[i][0]]
        m.append(eve)
    return m 

def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        o = [0, 0] # origin
        p = o[::] # position
        for m in moves:
            if m == 'R':
                p[1] = p[1] + 1
            if m == 'L':
                p[1] = p[1] - 1
            if m == 'U':
                p[0] = p[0] + 1
            if m == 'D':
                p[0] = p[0] - 1
                
        return o == p






























































































































































































































