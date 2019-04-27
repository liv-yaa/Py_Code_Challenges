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

    