# ANSWERS


# https://fellowship.hackbrightacademy.com/materials/challenges/binary-search/solution/index.html#binary-search-solution
def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    # START SOLUTION #

    higher_than = 0
    lower_than = 101
    guess = None

    while guess != val:
        num_guesses += 1
        guess = (lower_than - higher_than) // 2 + higher_than

        if val > guess:
            higher_than = guess

        elif val < guess:
            lower_than = guess

    # END SOLUTION

    return num_guesses


# More concise answer
def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    # START SOLUTION

    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])


def has_unique_chars(word):
    """Does word contains unique set of characters?"""

    # START SOLUTION

    unique_word = set(word)

    return len(unique_word) == len(word)


def is_prime(num):
    """Is a number a prime number?"""

    # START SOLUTION

    if num < 2:
        return False

    # This is a very naive check -- firstly, we could check once
    # for even numbers and then count up by twos. Secondly, we
    # only have to check up to sqrt(num) -- since if a number is
    # divisible by a number > its square root, the other divisor
    # would be definition be less than its square root.
    #
    # For our purposes, though, this is a reasonable answer for
    # an easy whiteboarding question.

    for n in range(2, num):
        if num % n == 0:
            return False

    return True 


def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number."""

    # START SOLUTION

    # Fail-fast optimization: since our list is sorted, if the first number
    # is bigger, a smaller number isn't in our list

    if nums[0] >= xnumber:
        return None

    # Optimization: if the last number isn't too big, it's the answer

    if nums[-1] < xnumber:
        return len(nums) - 1

    # Else, loop through and return the index right before the first number
    # that is too big

    for i, num in enumerate(nums):
        if num >= xnumber:
            return i-1




            
