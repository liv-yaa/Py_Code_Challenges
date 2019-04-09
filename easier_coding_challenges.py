"""
https://fellowship.hackbrightacademy.com/materials/challenges/_all.html#whiteboard-easier

"Easier":
- Add to Zero
- Anagram of Palindrome
- Binary Search
- Concatenate Lists
- Count List Recursively
- Days in Month
- Decimal to Binary
- Decode a String
- Find Lucky Numbers
- Find the Range
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


"""
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
    # dct = {}
    # n = len(A) // 2 # Array given is length 2n
    
    # for item in A:
    #     if item in dct:
    #         dct[item] += 1
    #     else:
    #         dct[item] = 1
    
    # for k, v in dct.items():
    #     # print(k, v)
    #     if v == n:
    #         return(k)

    # print(sum(A) - sum(set(A))) # the sum() function 

    return int((sum(A)-sum(set(A))) // (len(A)//2-1))
            




# Doctest Section:
if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')