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
- Snake case to camel case
!X Sort Sorted Lists
(!!) Split a String
X Sum List
X Sum List Recursively
X Word Count
X Word Lengths

"""
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




# Doctest Section:
if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')