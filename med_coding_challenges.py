"""
"Medium" Coding Challenges by HB
https://fellowship.hackbrightacademy.com/materials/challenges/_all.html#medium

X Anagram of Palindrome
X Balanced Parentheses          
!X Binary Search - still in prog
X Count List Recursively
!X Decode a String - still in prog
- Lazy Lemmings
!X Leaping Lemur
- Missing Number
- Mode
- Print Digits Backwards
- Print List Recursively
- Recursive Index
- Remove Linked List Node       
- Reverse Linked List
- Reverse a String Recursively
!X Sort Sorted Lists
- Split a String
X Sum List Recursively


"""

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


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?
    
    >>> has_balanced_parens("()")
    True
    >>> has_balanced_parens("")
    True
    >>> has_balanced_parens("(Oh Noes!)(")
    False
    >>> has_balanced_parens("((There's a bonus open paren here.)")
    False
    >>> has_balanced_parens(")")
    False
    >>> has_balanced_parens("(")
    False
    >>> has_balanced_parens("(This has (too many closes.) ) )")
    False
    >>> has_balanced_parens("Hey...there are no parens here!")
    True

    """

    countL = 0
    countR = 0

    for char in phrase:
        if char == '(':
            countL += 1

        elif char == ')':
            countR += 1


    return countL == countR


def has_balanced_parens2(phrase):
    """ HB SOLUTION
    Does a string have balanced parentheses?
    
    >>> has_balanced_parens2("()")
    True
    >>> has_balanced_parens2("")
    True
    >>> has_balanced_parens2("(Oh Noes!)(")
    False
    >>> has_balanced_parens2("((There's a bonus open paren here.)")
    False
    >>> has_balanced_parens2(")")
    False
    >>> has_balanced_parens2("(")
    False
    >>> has_balanced_parens2("(This has (too many closes.) ) )")
    False
    >>> has_balanced_parens2("Hey...there are no parens here!")
    True

    """

    parens = 0

    for char in phrase:

        if char == '(':
            parens += 1

        elif char == ')':
            parens -= 1

            if parens < 0:
                # We can never close more than we open
                return False

    # Make sure we have none left
    # if parens > 0:
    #     return False

    # else:
    #     return True 

    return (parens <= 0)


def lemmings(num_holes, cafes):
    """
    @num_holes - how many holes there are (there is a lemming in each hole)
    @cafes - a sorted list of the indices of the cafes in num_holes, with each num appearing
    at least once.
    Find out maximum distance any given lemming needs to travel to get to a cafe

    # >>> lemmings(1, [0]) # l = [1]
    # 0
    # >>> lemmings(2, [1]) # l = [0, 1]
    # 1    
    # >>> lemmings(2, [0, 1]) # l = [1, 1]
    # 0    
    # >>> lemmings(3, [2]) # l = [0, 0, 1]
    # 2   
    # >>> lemmings(3, [1]) # l = [0, 1, 0]
    # 1
    # >>> lemmings(3, [0, 1, 2]) # l = [1, 1, 1]
    # 0
    # >>> lemmings(4, [2]) # l = [0, 0, 1, 0]
    # 2   
    # >>> lemmings(4, [3]) # l = [0, 0, 0, 1]
    # 3
    # >>> lemmings(4, [0, 1, 2, 3]) # l = [1, 1, 1, 1]
    # 0


    """
    # Create list of lemmings and cafes (l)
    l = [0 for i in range(0, num_holes)]
    for cafe in cafes:
        l[cafe] = 1

    print('l', l)


    # Iterate through it, saving max of all min distances
    max_of_min_dist = 0

    for lem1 in l:

        # For each lemming, find the closest cafe:

        for lem2 in l:

            if lem2 == 1:
            
                dist = abs(lem1 - lem2)
                print('dist', dist)
                if dist > min_dist:
                    min_dist = dist 

                    print('new min_dist', min_dist)

        print('Overall min_dist', min_dist)


        if min_dist > max_of_min_dist:
            max_of_min_dist = min_dist

            print('new max_dist', max_of_min_dist)




    return max_of_min_dist


def lemur(branches):
    """ Return number of jumps needed.
    A lemur wants to jump across a span in the forest on branches. 
    She can jump 1 or 2 branches at a time. 
    >>> lemur([0])
    0
    >>> lemur([0, 0])
    1
    >>> lemur([0, 0, 0])
    1
    >>> lemur([0, 1, 0])
    1
    >>> lemur([0, 0, 1, 0])
    2
    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
    """

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"


    at = 0
    jumps = 0

    while at < len(branches) - 1:

        # Try to jump 2
        at += 2

        if at >= len(branches) or branches[at] == 1:

            # illegal to jump 2 so jump 1
            at -= 1

        # Increment
        jumps += 1

    return jumps


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


# def decode(s):
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



#     # >>> decode("h1ae2bcy")
#     # 'Invalid'
#     # >>> decode("7h1ae277")
#     # 'Invalid'
#     # >>> decode("")
#     # 'Invalid'
#     # >>> decode("h")
#     # 'Invalid'
#     # >>> decode("h1ae2bcy")
#     # 'Cannot convert integer, Invalid '

#     """
#     decoded = ""


#     if len(s) < 2:
#         return 'Invalid'
#     # Else, if len is 2 or more,

#     # Initialize i (index of number) and j (index of letter)
#     i = 0
    

#     while i < len(s) - 1:
#         numb = s[i]
#         char = s[i + 1]

#         print('numb', numb)
#         print('char', char)

#         # Find the next int
#         try:
#             numb = int(numb)
#             print('numb', numb)

#             # i += numb
#             # j += numb

#             # print('new numb ', s[i])


#         except TypeError:

        
#             print('type error')
            
#             gi += 1
#         decoded += char

#     return decoded



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


    return outlist # Come back


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


import math
import os
import random
import re
import sys

# From hackerranke - https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    """ calculate the absolute difference between the sums of its diagonals. 
        so, you just need the abs diff of four corners
    """
    d1 = 0 #[0][0], [1][1], [2][2], ...
    d2 = 0 #[0][n - 1], [1][n - 2], [2][n - 3], [n - 1][0]

    for i in range(n):
        d1 += arr[i][i]
        d2 += arr[i][n - 1 - i]

    return abs(d1 - d2)


""" BST Validator is it valid? https://fellowship.hackbrightacademy.com/materials/challenges/bst-valid/index.html#bst-valid
"""
class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):
        """Is this tree a valid BST?

        >>> t = Node(4,
        ...       Node(2, Node(1), Node(3)),
        ...       Node(6, Node(5), Node(7))
        ... )

        >>> t.is_valid()
        True

        >>> t = Node(4,
        ...       Node(2, Node(3), Node(3)),
        ...       Node(6, Node(5), Node(7))
        ... )

        >>> t.is_valid()
        False

        >>> t = Node(4,
        ...       Node(2, Node(1), Node(3)),
        ...       Node(6, Node(1), Node(7))
        ... )

        >>> t.is_valid()
        False

        """

















# Doctest Section:
if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')
