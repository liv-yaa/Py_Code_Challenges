"""

"Easier" https://fellowship.hackbrightacademy.com/materials/challenges/_all.html#whiteboard-easier
:
X Add to Zero
X Anagram of Palindrome
!X Binary Search
X Concatenate Lists
X Count List Recursively
X Days in Month
- Decode a String # COME BACK TO THIS
X Find Lucky Numbers
X Find the Range
- FizzBuzz
- Has More Vowels
- Has Unique Characters
- Is Number Prime?
- Is Palindrome?
- Largest Smaller Than
- Lazy Lemmings
- Leaping Lemur
- Leet Speak
- Longest Word
- Max Number
- Max of Three
- Missing Number
- Pangram
- Pig Latin
- Prime Number Generator
- Print Digits Backwards
- Print List Recursively
- Recursive Index
- Remove Duplicates
- Remove Linked List Node
- Replace Vowels
- Reverse LinkedList
- Reverse LinkedList In Place
- Reverse a String Recursively
- Show Even Numbers
X Snake case to camel case
!X Sort Sorted Lists
!X Split a String
X Sum List
X Sum List Recursively
X Word Count
X Word Lengths

Leetcode problems:
X numJewelsInStones
X repeatedNTimes


"""

import random, math

def add_to_zero(nums):
    """ Given a list of ints, return true if any two nums in list sum to 0.
    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True
    """
    set_nums = set(nums) # Gives us faster lookup time in O(1) rather than O(n)

    for n in nums:
        if -n in set_nums:
            return True

    return False


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?
    - A palindrome is a word that reads the same forward and backwards (eg, “racecar”, “tacocat”). 
    - An anagram is a rescrambling of a word (eg for “racecar”, you could rescramble this as “arceace”).

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False
    """
    # Create a word count dictionary
    d = {}
    for char in word:
        d[char] = d.get(char, 0) + 1


    # A palindrome will have a dic that is (all even counts; 0 or 1 only odd count)
    # not a palindrome will have 2 or more odd counts
    odd_counts = 0

    for count in d.values():
        if count % 2 == 1:
            odd_counts += 1


    return (odd_counts < 2)


def binary_search(val):
    """
    Using binary search, find val in range 1-100. Return # of guesses.

    Search a sorted list in O(log n) time, a large improvement over scanning every item in the list (which would be O(n) time).
    To do this, you examine the middle item and, 
    - if the sought-for value is smaller, move halfway to the left. 
    - If the sought-after value is larger, move halfway to the right.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
    """
    assert 0 < val < 101, "Val must be between 1-100"

    # Initialize the guess counter
    num_guesses = 0

    # Set ceiling and floor. and the 'guess' variable
    higher_than = 0
    lower_than = 101
    guess = None

    # 
    while guess != val:

        # Increment counter
        num_guesses += 1

        # Guess a guess
        guess = (lower_than - higher_than) // 2 + higher_than

        if val > guess:
            higher_than = guess

        elif val < guess:
            lower_than = guess

        # When val == guess, it will break


    return num_guesses


def concat_lists(list1, list2):
    """Combine lists.
    https://fellowship.hackbrightacademy.com/materials/challenges/concat-lists/index.html#concat-lists

    >>> concat_lists([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> concat_lists([], [1, 2])
    [1, 2]
    >>> concat_lists([1, 2], [])
    [1, 2]
    >>> concat_lists([], [])
    []

    """

    for item in list2:
        list1.append(item)
    return list1


def count_recursively(lst):
    """Return number of items in a list, using recursion.
    >>> count_recursively([])
    0
    >>> count_recursively([1, 2, 3])
    3
    >>> count_recursively([1])
    1
    >>> count_recursively([1, 3])
    2

    """

    if len(lst) == 0:
        return 0

    return count_recursively(lst[1:]) + 1


def is_leap_year(year):
    """ HELPER FUNC GIVEN FOR DAYS_IN_MONTH
    Is this year a leap year?

    Every 4 years is a leap year::

        >>> is_leap_year(1904)
        True

    Except every hundred years::

        >>> is_leap_year(1900)
        False

    Except-except every 400::

        >>> is_leap_year(2000)
        True
    """
    try:
        year = int(year)
        # print('type conversion int', year)

        if year % 400 == 0:
            return True

        if year % 100 == 0:
            return False

        if year % 4 == 0:
            return True

    except:
        return 'Cannot convert year to int'


def days_in_month(date):
    """How many days are there in a month?

    >>> days_in_month("02 2015")
    28
    >>> days_in_month("02 2016")
    29
    >>> days_in_month("03 2016")
    31
    >>> days_in_month("04 2016")
    30
    >>> days_in_month("")
    0
    >>> days_in_month("05 2019 999 45")
    0


    
    """

    # Create sets with matching numbers
    l31 = {'01', '03', '05', '07', '08', '10', '12'}
    l30 = {'04', '06', '09', '11'}

    # Try to split input into a list
    monthyear = date.split(" ")
    if len(monthyear) != 2:
        # Invalid format for input
        return 0

    month = monthyear[0]
    year = monthyear[1]   

    if month == '02':
        if is_leap_year(year):
            return 29
        else:
            return 28

    elif month in l31:
        return 31

    elif month in l30:
        return 30

    return 0


def decode(s):
    #     """ Decode a string. A valid code is a sequence of numbers and letters, 
    #     always starting with a number and ending with letter(s).
    #     Each number tells you how many characters to skip before finding a good letter. 
    #     After each good letter should come the next next number.

    #     >>> decode("0h")
    #     'h'
    #     >>> decode("2abh")
    #     'h'
    #     >>> decode("0h1ae2bcy")
    #     'hey'
    #     >>> decode("h1ae2bcy")
    #     'Invalid'
    #     >>> decode("7h1ae277")
    #     'Invalid'
    #     >>> decode("")
    #     'Invalid'
    #     >>> decode("h")
    #     'Invalid'
    #     >>> decode("h1ae2bcy")
    #     'Cannot convert integer, Invalid '

    #     """
    #     decoded = ""


    #     if len(s) < 2:
    #         return 'Invalid'
    #     # Else, if len is 2 or more,

    #     # Initialize i (index of number) and j (index of letter)
    #     i = 0
    #     j = 1

    #     while i < len(s) - 1:

    #         numb = int(s[i])
    #         char = s[i + j]

    #         if type(char) == chr:
    #             decoded += char

    #         i += numb
    #         j = 1
    pass # COME BACK TO THIS


def lucky_numbers(n):
    """ Return n unique random numbers from 1-10 (inclusive).
    # >>> lucky_numbers(2)
    # [3, 7]
    >>> lucky_numbers(0)
    []
    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    """
    out = set() # A set will not allow duplicate objects

    while len(out) <= n and n > 0:

        # Generate a random number and add to set
        out.add(random.randrange(1, 11))

        if len(out) == n:
            break

    return list(out) # Type conversion - O(n)


def find_range(nums):
    """ Given list of numbers, return smallest & largest number as a tuple.

    >>> find_range([3, 4, 2, 5, 10])
    (2, 10)
    >>> find_range([43, 3, 44, 20, 2, 1, 100])
    (1, 100)
    >>> find_range([])
    (None, None)
    >>> find_range([7])
    (7, 7)

    """

    smallest = None
    largest = None

    if len(nums) == 1:
        smallest, largest = nums[0], nums[0]

    elif len(nums) > 1:
        smallest = nums[0]
        largest = nums[1] 

        for n in nums:
            if n < smallest:
                smallest = n 

            if n > largest:
                largest = n

    return (smallest, largest)


def fizzbuzz(n):
    """ Count from 1 to 20 in fizzbuzz fashion.
    Each time through, if the number is evenly divisible by 3, say ‘fizz’. 
    If the number is evenly divisible by 5, say ‘buzz’. 
    If the number is evenly divisible by both 3 and 5, say ‘fizzbuzz’. 
    Otherwise, say the number.



    >>> fizzbuzz(20)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz

    """
    if n > 0:

        for i in range(1, n + 1):
            # print(i)

            if i % 15 == 0:
                print('fizzbuzz')

            elif i % 5 == 0:
                print('buzz')

            elif i % 3 == 0:
                print('fizz')

            else:
                print(i)


def has_more_vowels(word):
    """ Does word contain more vowels than non-vowels?

    >>> has_more_vowels("moose")
    True
    >>> has_more_vowels("mice")
    False
    >>> has_more_vowels("graph")
    False
    >>> has_more_vowels("yay")
    False
    >>> has_more_vowels("Aal")
    True

    """

    vow_count = 0 
    con_count = 0

    for char in word:

        if char.lower() in 'aeiou':
            vow_count += 1

        elif char.lower() in 'bcdfghjklmnpqrstvwxyz':
            con_count += 1

    return vow_count > con_count


def has_unique_chars(word):
    """ Does word contains unique set of characters? 

    >>> has_unique_chars("Monday")
    True
    >>> has_unique_chars("Moonday")
    False
    >>> has_unique_chars("")
    True
    >>> has_unique_chars("Bob")
    True

    """

    uni = {}

    for char in word:
        uni[char] = uni.get(char, 0) + 1

    for val in uni.values():
        if val != 1:
            return False 

    return True


def has_unique_chars2(word):
    """ Does word contains unique set of characters? 

    >>> has_unique_chars2("Monday")
    True
    >>> has_unique_chars2("Moonday")
    False
    >>> has_unique_chars2("")
    True
    >>> has_unique_chars2("Bob")
    True

    """

    uni = set(word)

    return len(uni) == len(word)


def is_prime(num):
    """Is a number a prime number?
    >>> is_prime(0)
    False

    >>> is_prime(1)
    False

    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(11)
    True

    >>> is_prime(999)
    False

    """
    if num == 0 or num == 1:
        return False

    elif num == 2:
        return True

    elif num > 2:

        divisors = [i for i in range(1, num + 1) if num % i == 0]

        return (len(divisors) == 2)  

    else:
        return False






def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.

    >>> show_evens([1, 2, 3, 4, 6, 8])
    [1, 3, 4, 5]

    >>> show_evens([])
    []

    >>> show_evens([1, 3, 5])
    []
    
    """
    outlist = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            outlist.append(i)


    return outlist


def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name.

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

    >>> snake_to_camel("_")
    ''
    
    >>> snake_to_camel("L_L")
    'LL'

    >>> snake_to_camel("")
    ''

    """
    
        
    if "_" in variable_name:

        if len(variable_name) > 0:

            index = variable_name.index("_")
            # print(index)

            if index > 0:

                before = variable_name[:index]
                after = variable_name[index + 1:]

                if len(after) > 0:

                    after = after[0].upper() + after[1:]

                return (before + after)
  
        return ""
        
    return variable_name


def snake_to_camel2(variable_name):
    """
    This is their more succinct solution https://fellowship.hackbrightacademy.com/materials/challenges/snake-to-camel/solution/index.html
    Given a variable name in snake_case, return camelCase of name.

    >>> snake_to_camel2("hi_balloonicorn")
    'hiBalloonicorn'

    >>> snake_to_camel2("_")
    ''
    
    >>> snake_to_camel2("L_L")
    'LL'

    >>> snake_to_camel2("")
    ''

    """ 
    words = variable_name.split("_")

    for i in range(1, len(words)):
        words[i] = words[i].capitalize()

    return "".join(words)


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    
    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]

    >>> sort_ab([2, 6, 8, 10], [1, 3, 5, 7])
    [1, 2, 3, 5, 6, 7, 8, 10]

    >>> sort_ab([2, 6, 8, 10], [])
    [2, 6, 8, 10]

    * solution * https://fellowship.hackbrightacademy.com/materials/challenges/sort-ab/solution/index.html

    """

    outlist = []

    ia = 0
    ib = 0

    while ia < len(a) and ib < len(b):

        if a[ia] < b[ib]:
            outlist.append(a[ia])
            ia += 1

        else:
            outlist.append(b[ib])
            ib += 1

    # Add any remaining items:
    outlist.extend(a[ia:])
    outlist.extend(b[ib:])


    return outlist


def split(astring, splitter):
    """Split a string by splitter and return list of splits.
    (Words like built in split() method! Dont use regex)

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']


    """
    lst = []
    index = 0

    # Get chunks of length l from astring:
    while index <= len(astring):

        curr = index
        index = astring.find(splitter, index)

        if index != -1:
            lst.append(astring[curr:index])
            index += len(splitter)

        else:
            lst.append(astring[curr:])
            break

    return lst


def sum_list_n(num_list):
    """Return the sum of all numbers in list.
    >>> sum_list_n([5, 3, 6, 2, 1])
    17
    >>> sum_list_n([5, 5])
    10
    >>> sum_list_n([-5, 10, 4])
    9
    >>> sum_list_n([20])
    20
    >>> sum_list_n([])
    0

    ALL TESTS PASSED
    """
    total = 0
    for num in num_list:
        total += num
    return total


def sum_list(nums):
    """Using recursion, return the sum of numbers in a list.
    >>> sum_list([5, 3, 6, 2, 1])
    17
    >>> sum_list([5, 5])
    10
    >>> sum_list([-5, 10, 4])
    9
    >>> sum_list([20])
    20
    >>> sum_list([])
    0

    ALL TESTS PASSED
    """
    if len(nums) > 0:
        total = nums[0]

        if len(nums) > 1:
            return sum_list(nums[1:]) + total
        else:
            return total

    else:
        return 0


def word_count(phrase):
    """Count words in a sentence, and print in ascending order.
    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2

    ALL TESTS PASSED
    """

    # Data structure = dictionary. In Python3 we can count on it being ordered
    dictionary = {}

    # Split string into list and sort:
    lst = sorted(phrase.split())

    for word in lst:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    for key,value in dictionary.items():
        print(key + ":", value)


def word_lengths(sentence):
    """Get dictionary of word-length: {words}.
    * Note for Python3.6 we can count on order of dicts

    ex. answer = word_lengths("cute cats chase fuzzy rats")
    {4: {'cute', 'cats', 'rats'}, 5: {'fuzzy', 'chase'}}

    Did not pass becasue I dont have the doctest savvy but it is correct
    """

    # Create a dict:
    dct = {}

    lst = sentence.split()

    for word in lst:
        if len(word) in dct:
            dct[len(word)].add(word)
        else:
            dct[len(word)] = {word}

    print( dct)

    #     *** Note: They did not recommend
    # lengths.setdefault(len(word), set()).add(word) 
    # ***   


def numJewelsInStones(J: str, S: str) -> int:
    """
    Leetcode #771
    You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

    The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

    Example 1:
    >>> numJewelsInStones("aA", "aAAbbbb")
    3

    Input: J = "z", S = "ZZ"
    Output: 0
    """
    count = 0
    for letter in S:
        if letter in J:
            count = count + 1
    return count


def repeatedNTimes(A) -> int:
    """
    Leetcode problem 961
    In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

    Return the element repeated N times.


    >>> repeatedNTimes([1,2,3,3])
    3

    >>> repeatedNTimes([2,1,2,5,3,2])
    2

    >>> repeatedNTimes([5,1,5,2,5,3,5,4])
    5

    """    
    counts = dict()
    for i in A:
        counts[i] = counts.get(i, 0) + 1 # Study!
    
    for k, v in counts.items():
        if v == len(A) // 2:
            return(k)


def sortedSquares(A):
    
        return sorted(item ** 2 for item in A)

        
def sortArrayByParity(A):
    
    out = [even for even in A if even % 2 == 0]
    out.extend([odd for odd in A if odd % 2 == 1])
    return out


def toLowerCase(str: str) -> str:
    
    return "".join([l.lower() for l in str])


def numUniqueEmails(emails) -> int:
        
    """
    Every email consists of a local name and a domain name, separated by the @ sign.

    For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

    Besides lowercase letters, these emails may contain '.'s or '+'s.

    If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

    If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

    It is possible to use both of these rules at the same time.

    Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

    Example 1:

    Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    Output: 2
    Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
    """
    uniques = set()
    
    for email in emails:
        e = email.split("@")
        local = e[0]
        domain = e[1]
                    
        if '+' in local:
            local = local[:local.index('+')]
        
        if '.' in local:
            local = "".join(local.split("."))
        
        uniques.add(local + "@" + domain)
    
    return len(uniques)


def addStrings(num1: str, num2: str) -> str:
    summer = 0
    ints = "0123456789"
    
    for num in [num1, num2]:

        i = 0
        j = 1
        while i < len(num):
            z = num[len(num) - 1 - i]
            x = ints.index(z)
            summer += x * j

            # Increment
            i += 1
            j *= 10
                
    return str(summer)


def flipAndInvertImage(A):
    """
    Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

    To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

    To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
    """
    out = []
    for sublist in A:
        rev = sublist[::-1]
        rev_out = []
        
        for i in range(len(rev)):
            if rev[i] == 0:
                rev_out.append(1)
            elif rev[i] == 1:
                rev_out.append(0)
                
        out.append(rev_out)
        
    return out
        

def judgeCircle(moves: str) -> bool:
    """
    https://leetcode.com/problems/robot-return-to-origin/
    """
    
    return (moves.count('D') == moves.count('U') and moves.count('L') == moves.count('R'))     


def diStringMatch(S: str):
    """
        
    Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

    Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

    If S[i] == "I", then A[i] < A[i+1]
    If S[i] == "D", then A[i] > A[i+1]


    ** I looked up solution https://leetcode.com/problems/di-string-match/solution/
    """
    # Initialize indices:
    lo = 0
    hi = len(S)
    ans = []

    # Add to ans list, taking from highest and lowest each time depending on what is specified:
    for x in S:
        if x == "I":
            ans.append(lo)
            lo += 1
        else:
            ans.append(hi)
            hi -= 1
        
    return ans + [lo] # Study
        

def minDeletionSize(A) -> int:
    """
    We are given an array A of N lowercase letter strings, all of the same length.

    Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

    For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].  (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)

    Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.

    Return the minimum possible value of D.length.

    Input: ["cba","daf","ghi"]
    Output: 1
    Explanation: 
    After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
    If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.

    Input: ["a","b"]
    Output: 0
    Explanation: D = {}

    Input: ["a","b"]
    Output: 0
    Explanation: D = {}
    
    ** Looked up answer **https://leetcode.com/problems/delete-columns-to-make-sorted/submissions/


    """
    ans = 0
    
    for i in range(len(A[0])):
        prev = A[0][i]
        
        for j in range(1, len(A)):
            if prev > A[j][i]:
                ans += 1
                break
            else:
                prev = A[j][i]
        
            
                
    return ans
    

def sortArrayByParityII(A):
    
    """
    https://leetcode.com/problems/sort-array-by-parity-ii/submissions/
    Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

    Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

    You may return any answer array that satisfies this condition.
    Example 1:
    Input: [4,2,5,7]
    Output: [4,5,2,7]
    """
    out = []
    evens = [a for a in A if a % 2 == 0]
    odds = [a for a in A if a % 2 == 1]
    
    for i in range(len(evens)):
        
        out.append(evens[i])
        out.append(odds[i])
        
    return out


def canPlaceFlowers(flowerbed, n) -> bool:
    """
    Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

    Examples:
    # >>> canPlaceFlowers([1,0,0,0,1], n = 1)
    # Output: True
    # >>> canPlaceFlowers([1,0,0,0,1], n = 2)
    # False
    
    """
    print(n)


    return False
    
        
def countingValleys(n, s):
    """
    return an integer that denotes the number of valleys Gary traversed

    n: the number of steps Gary takes
    s: a string describing his path

    >>> countingValleys(8, 'UDDDUDUU')
    1

    >>> countingValleys(12, 'DDUUDDUDUUUD')
    2

    >>> countingValleys(5, 'UUDUU')
    0

    """
    L=0
    V=0
    for st in s:
        if st == 'U':
            L += 1
            if L == 0:
                V += 1
        else:
            L -= 1
            
    return V
       
            
def jumpingOnClouds(c):
    """
    return the minimum number of jumps req'd to traverse array.
    c: an array of binary integers, 0 is legal and 1 is illegal
    jumps can be +2 or +1 only.

    >>> jumpingOnClouds(c=[0, 0, 1, 0, 0, 1, 0])
    4

    >>> jumpingOnClouds(c=[0, 0, 0, 0, 1, 0])
    3

    https://www.hackerrank.com/challenges/jumping-on-the-clouds/
    """

    avoid = [i for i in range(len(c)) if c[i] == 1]
    l = len(c)

    jumps = 0
    j = 0 # First index has to be legal
    while j < len(c):
        # Try to jump 2
        if (j + 2) not in avoid and (j + 2) < len(c):
            j = j + 2
            jumps += 1
            if j == len(c):
                break
        
        # Try to jump 1
        elif (j + 1) not in avoid and (j + 1) < len(c):
            j = j + 1
            jumps += 1
            if j == len(c):
                break

        else:
            break
        
    return jumps

def repeatedString(s, n):
    """ 
    Count the occurances of 'a' in string s, repeated infinitely,
    for the chunk up to n total.

    >>> repeatedString('aba', 10)
    7

    >>> repeatedString('a', 1000000000000)
    1000000000000

    Looked up answer :/
    https://www.hackerrank.com/challenges/repeated-string/forum
    """
    count = 0

    count = s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
    # print(n % len(s)) # 10 % 3 = 1, AND # 1000000000000 % 1 = 0 

    # chunk = s[:n % len(s)] # [a] AND [], respectively
    # print(list(chunk))

    # print(chunk.count('a'))

    # print(n // len(s))
    return count


# from collections import Counter

def checkMagazine(magazine, ransom):
    """
    https://www.hackerrank.com/challenges/ctci-ransom-note/problem?isFullScreen=true
    
    >>> checkMagazine('two times three is not four', 'two times two is four')
    'No'

    >>> checkMagazine('ive got a lovely bunch of coconuts', 'ive got some coconuts')
    'No'

    >>> checkMagazine('give me one grand today night', 'give one grand today')
    'Yes'

    """

    result = True

    for word in ransom.split():
        if (word not in magazine.split()) or (ransom.split().count(word) != magazine.split().count(word)):
            result = False

    return 'Yes' if result else 'No'





class InterestingCodingNotes:
    pass        
    """ NOTABLE PY Built In FUNCTIONS!!! 




    >>> bin(4) # convert decimal to binary
    '0b100'






    ## "Boolean Logical "Short Circuiting" - an interesting idomatic way to use "or" in python:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children or [] 


    -- Equivalent to:
    def __init__(self, data, children=None):
        self.data = data
        if children is None:
            # make sure we make a new, separate empty list
            self.children = []
        else:
            self.children = children






    ## 'is' operator for boolean
    >>> snape.children is flitwick.children
    False








    ## In trees:

    ## - a "Depth First Search" uses a STACK
            - This is because we want to get First In First Out
            - Search through all chilren recursively before we move to the next sibling 

    ## - a "Breadth First Search" uses a QUEUE
            - We want to get Last In First Out
            - Search through all siblings before going on to the next child.






    ## Q: Which methods are in Node class? Which methods are in Tree class?
    You may find it useful to make a Tree class sometimes, though – but you’ll 
    often delegate methods like find onto the root node. This lets you use them 
    for the entire tree, while also being able to search directly on a lower-level node.

        class Tree(object):  # ...
        def find_in_tree(self, data):
            ## Return node object with this data.
            ## Start at root. Return None if not found.
        
            return self.root.find(data)


        class Node(object):  # ...
        def find(self, data):
            # Return node object with this data.
            # Start here. Return None if not found.

            to_visit = [self]

            while to_visit:
                current = to_visit.pop()

                if current.data == data:
                    return current

                to_visit.extend(current.children)







    ## SET NOTATION PY3 ##

        A | B 
        A.union(B)
        Returns a set which is the union of sets A and B.
        
        A |= B 
        A.update(B)
        Adds all elements of array B to the set A.
        
        A & B 
        A.intersection(B)
        Returns a set which is the intersection of sets A and B.
        
        A &= B 
        A.intersection_update(B)
        Leaves in the set A only items that belong to the set B.
        
        A - B 
        A.difference(B)
        Returns the set difference of A and B (the elements included in A, but not included in B).
        
        A -= B 
        A.difference_update(B)
        Removes all elements of B from the set A.
        
        A ^ B 
        A.symmetric_difference(B)
        Returns the symmetric difference of sets A and B (the elements belonging to either A or B, but not to both sets simultaneously).
        
        A ^= B 
        A.symmetric_difference_update(B)
        Writes in A the symmetric difference of sets A and B.
        
        A <= B 
        A.issubset(B)
        Returns true if A is a subset of B.
        
        A >= B 
        A.issuperset(B)
        Returns true if B is a subset of A.
        
        A < B
        Equivalent to A <= B and A != B
        
        A > B
        Equivalent to A >= B and A != B





    """


# Doctest Section:
if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')