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
- Sort Sorted Lists
- Split a STring
X Sum List
X Sum List Recursively
X Word Count
- Word Lengths

"""

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

    >>> answer = word_lengths("cute cats chase fuzzy rats")
    {4: {'cute', 'cats', 'rats'}, 5: {'fuzzy', 'chase'}}

    *** Note: They did not recommend
    lengths.setdefault(len(word), set()).add(word) 
    ***   
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




# Doctest Section:
if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')