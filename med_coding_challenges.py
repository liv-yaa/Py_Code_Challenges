"""
"Medium" Coding Challenges by HB
https://fellowship.hackbrightacademy.com/materials/challenges/_all.html#medium

X Anagram of Palindrome
- Balanced Parentheses
!X Binary Search - still in prog
X Count List Recursively
!X Decode a String - still in prog
- Lazy Lemmings
- Leaping Lemur
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
    pass # COME BACK TO THIS # Come back


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


