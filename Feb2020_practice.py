# Feb2020_practice.py

def matchingStrings(strings, queries):
	""" """
    results = [None] * len(queries)
    for i, q in enumerate(queries):
        results[i] = strings.count(q)
    return results

import textwrap

def wrap(s, w):
    return textwrap.fill(s,w)

def swap_case(s):
    out = ''
    for c in s:
        if c.isupper():
            out += c.lower()
        elif c.islower():
            out += c.upper()
        else:
            out += c

    return out

# if __name__ == '__main__':
#     s = 'HackerRank.com presents "Pythonist 2".'
#     result = swap_case(s)
#     print(result)


def text_align(thickness):
	# thickness = int(input()) #This must be an odd number
	c = 'H'

	#Top Cone
	for i in range(thickness):
	    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

	#Top Pillars
	for i in range(thickness+1):
	    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

	#Middle Belt
	for i in range((thickness+1)//2):
	    print((c*thickness*5).center(thickness*6))    

	#Bottom Pillars
	for i in range(thickness+1):
	    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

	#Bottom Cone
	for i in range(thickness):
	    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


def is_leap(year):    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def fams(k, elems):
	# Bad answer!
	k = input()
    elems = [int(x) for x in input().strip().split(' ')]
    print(fams(k, elems))
    # Create a counts dictionary
    cts = {}
    for e in elems:
        cts[e] = cts.get(e, 0) + 1

    # Get the one item in dictionary that has value != 0
    ans = [None, None]
    for e, v in cts.items():
        if v != k:
            ans = (e, v)
    return ans[0]


def captain_room_ans():
	# Answer from https://www.hackerrank.com/challenges/py-the-captains-room/editorial
	K = int(raw_input())

	#Step 1: Gets the input
	roomList = map(int, raw_input().split())

	#Step 2: create a set from input list
	roomSet = set(roomList) 

	#Step 3: Add up all items in the list and set respectively
	sumRoomSet = sum(roomSet) 
	sumRoomList = sum(roomList) 

	# Step 4: 
	temp = sumRoomSet * K - sumRoomList 

	# Step 5
	answer = temp / (K - 1) 

	# Step 6
	print answer
	K = int(input())
	set_S = set()
	sumlist_S = 0
	for i in input().split():
	    I = int(i)
	    set_S.add(I)
	    sumlist_S += I

	print((sum(set_S)*K - sumlist_S)//(K-1)) 


def captain_room():
	rooms = "1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 "
	k = 5 # actually input()
	roomList = rooms.strip().split(' ') # actually input()
	print(roomList)


# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
import calendar

def dayOnDate(gd):
    """ Given a date `gd`, find which day is on that date. """
    DAYS = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    gd = gd.split(' ')

    if len(gd) > 2:
        c = list(calendar.Calendar().itermonthdays2(int(gd[2]), int(gd[0])))
        for it in c:
            if it[0] == int(gd[1]):
                return DAYS[it[1]]
    return None

if __name__ == '__main__':
    givenDate = input()
    print(dayOnDate(givenDate))


# https://www.hackerrank.com/challenges/capitalize
def capitalizeName(s):
    """ Ensure that first, last name are capitalized """
    names = s.split(' ')
    for i in range(len(names)):
        n = names[i]
        if n != '':
            names[i] = n[0].upper() + n[1:]
    return ' '.join(names)


def exceptions():
    # https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

    l = int(input())
    for _ in range(l):
        a, b = input().split()
        try:
            print(int(a) // int(b))
        except (ZeroDivisionError, ValueError) as e:
            print('Error Code:', e)


import re
def isValidRegex(string):
    # Check if a string is a valid regex or not
    # https://www.hackerrank.com/rest/contests/master/challenges/incorrect-regex/hackers/tssads/download_solution

    t = int(input())
    for _ in range(t):
        try:
            re.compile(input()) # Cool trick (from re library) - use the .compile function to throw an error if the thing is not a regex!
            print(True)
        except re.error:
            print(False)




"""
`reduce`
    - a function that applies a function of 2 args
    cumulatively on a list of objects in succession from left to right
    to reduct it to one value 

        from functools import reduce

        reduce(lambda x, y: x + y, [1, 2, 3])
        >>> 6
        (because 1 + 2 = 3, 3 + 3 = 6)

    - You can also define an initial value

        reduce(lambda x, y: x + y, [1, 2, 3], -3)
        >>> 6
        (because -3 + 1 = -2, -2 + 2 = 0, 0 + 3 = 3)
        (really just equivalent to adding a value to beginning of list)

    - You can import functions to 
        from fractions import gcd
        reduce(gcd, [2, 4, 8], 3)
        >>> 1

    https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

"""
# The Fractions module provides support for rational number arithmetic.
    # f = Fraction(numerator=0, denominator=1)
    # https://docs.python.org/2/library/fractions.html

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)    
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)








"""
itertools.combinations(iterable, r)

    This tool returns the  length subsequences of elements from the input iterable.

    Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order

"""
from itertools import combinations
def sortedComs():
    #Your task is to print all possible size k combinations of the string in lexicographic sorted order.
    x, y = input().split()
    for l in range(1, int(y) + 1):
        sc = [sorted(com) for com in sorted(list(combinations(x, l)))]
        for item in sorted(sc):
            print(''.join(item))


"""
itertools.combinations_with_replacement(iterable, r)

    This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
    Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order

"""
from itertools import combinations_with_replacement
def sortedComs():
    #Your task is to print all possible size k combinations of the string in lexicographic sorted order.
    x, y = input().split()
    for item in sorted([sorted(o) for o in sorted(combinations_with_replacement(x, int(y)))]):
        print(''.join(item))
    



from itertools import groupby
def charCtsString():
    # https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
    st = input()
    a = [] # a list to store tuples (n, ct)
    i = 1 # the index in st
    ct = 1 # Count 

    while i < len(st):
        if st[i] == st[i - 1]:
            ct += 1
        else:
            a.append((ct, int(st[i - 1])))
            ct = 1
        i += 1

    a.append((ct, int(st[i - 1])))

    for x in a:
        print(x, end=' ')


from itertools import combinations
def probability(ln, elems, k):
    # Select any k integers with a uniform probability from the list
    # Find prob that at least one will contain 'a'
    ais = [i for i in range(ln) if elems[i] == 'a']
    c = list(combinations([i for i in range(ln)], k))
    return sum([1 for com in c if (set(com) & set(ais)) != set()]) / len(c)



from itertools import product
def maximizeFunc():
    """
    https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
        For f(X) = X^2,
        Given a list of lists,
        pick one value from the list so that the value is maximized.
        S = [f(X1) + f(X2) + ... + f(Xk)] * M

        Where Xi is the element picked from the ith list.
    """
    k, m = [int(u) for u in input().split()]
    lsts = [sorted([(int(x) ** 2) % m for x in input().split()[1:]]) for _ in range(k)]
    return max([sum(t) % m for t in itertools.product(*lsts)])



"""
re
    re.findall()

        - Returns all Non-overlapping patterns in a string as a 
        list of strings

            >>> import re
            >>> re.findall(r'\w','http://www.hackerrank.com/')
            ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

        
    re.finditer()

        - Returns an iterator yielding MatchObject instances over
        all non-overlapping matches for the `re` pattern in the string

            >>> import re
            >>> re.finditer(r'\w','http://www.hackerrank.com/')
            <callable-iterator object at 0x0266C790>
            >>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
            ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']


"""

import re
def findAllRegex():
    # Given S, a string consisting of chars/symbols 
    # Find all substrings that contain 2 or more vowels, that lie between 2 consonants
    # Print matched substrings in order of occurance on separate lines
    # If no match found, print -1
    # S = input().strip()
    vows = 'AEIOUaeiou'
    cons = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'

    m = re.finditer(r'[^AEIOUaeiou +\-]([AEIOUaeiou]{2,})(?=[^AEIOUaeiou +\-])', input().strip())

    # print(list(m))

    found = 0
    for mm in m:
        print(mm.group(1))
        found = 1

    if found == 0:
        print('-1')


import re
def reStartEnd():
    """
    start() & end()
    These expressions return the indices of the start and end of the substring matched by the group.

    Given string S, find the indices of the start and end of string k in S. 
    """
    S = input()
    k = input()
    p = r'(?=%s)' % k

    if not re.search(p, S):
        print((-1, -1))

    for i in re.finditer(p, S):
        print((i.start(), i.start() + len(k) - 1))



























# def findAllRegex():
#     return input()

# if __name__ == '__main__':
#     print(findAllRegex())

