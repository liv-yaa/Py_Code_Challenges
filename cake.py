"""
Interview Cake - probs

"""

def binary_search(target, nums):
    """See if target appears in nums, Recursively

    Runtime is 

    https://www.interviewcake.com/question/python3/two-egg-problem

    >>> binary_search(10, [1, 2, 3, 4, 10, 5, 6, 7, 8, 9])
    True
    >>> binary_search(10, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    False



    """
    # Choose "walls" around the position of target
    
    floor_ix = -1 # -1 is to the left of the 0th index
    ceil_ix = len(nums) # Last index

    # If there is nothing between floor and ceil, the number must not be present
    while floor_ix + 1 < ceil_ix:

        # Find the index ~ halfway between flor and ceil
        distance = ceil_ix - floor_ix
        half_dist = distance // 2
        guess_ix = floor_ix + half_dist

        guess = nums[guess_ix]

        if guess == target:
            return True

        if guess > target:
            # Target is to the left, so move ceil to left
            ceil_ix = guess_ix

        else:
            # Target is to the right, so move floor to right
            floor_ix = guess_ix


    return False



def merge_sort(list_to_sort):
    """
    https://www.interviewcake.com/article/python/logarithms?course=fc1&section=algorithmic-thinking
    """
    # Base case: lists with fewer than 2 elements are sorted
    if len(list_to_sort) < 2:
        return list_to_sort

    # Step 1: divide the list in half
    # We use integer division, so we'll never get a "half index"
    mid_index = len(list_to_sort) / 2
    left  = list_to_sort[:mid_index]
    right = list_to_sort[mid_index:]

    # Step 2: sort each half
    sorted_left  = merge_sort(left)
    sorted_right = merge_sort(right)

    # Step 3: merge the sorted halves
    sorted_list = []
    current_index_left = 0
    current_index_right = 0

    # sortedLeft's first element comes next
    # if it's less than sortedRight's first
    # element or if sortedRight is exhausted
    while len(sorted_list) < len(left) + len(right):
        if ((current_index_left < len(left)) and
                (current_index_right == len(right) or
                 sorted_left[current_index_left] < sorted_right[current_index_right])):
            sorted_list.append(sorted_left[current_index_left])
            current_index_left += 1
        else:
            sorted_list.append(sorted_right[current_index_right])
            current_index_right += 1
    return sorted_list



def merge_ranges(meetings):
    """
    A feature to see the times in a day when everyone is available.
    In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). 
    These integers represent the number of 30-minute blocks past 9:00am.
    https://www.interviewcake.com/question/python3/merging-ranges?course=fc1&section=array-and-string-manipulation    
    
    >>> merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    """

    # Merge meeting ranges
    # Want to do O(n) - What if we sorted our list of meetings by start time?

    sort_meetings = sorted(meetings)
    

    merged_meetings = [sort_meetings[0]]
    
    
    for curr_start, curr_end in sort_meetings[1:]:
        last_merged_start, last_merged_end = merged_meetings[-1]
        
        if (curr_start <= last_merged_end):
            merged_meetings[-1] = (last_merged_start, max(last_merged_end, curr_end))
            
        else:
            merged_meetings.append((curr_start, curr_end))
    


    return merged_meetings



def reverse_list(lst):
    """
    Write a function that takes a list of characters and reverses the letters in place. ↴

    (note lists are mutable but strings are not)

    >>> reverse_list(['a', 'b', 'c'])
    ['c', 'b', 'a']
    >>> reverse_list(['a', 'b'])
    ['b', 'a']
    >>> reverse_list([])
    []
    >>> reverse_list(['c'])
    ['c']

    """

    left = 0
    right = len(lst) - 1

    while left < right:

        # Swap, move toward middle:

        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    

    return lst

# def reverse_characters(message, left_index, right_index):
#     # Walk towards the middle, from both sides
#     while left_index < right_index:
#         # Swap the left char and right char
#         message[left_index], message[right_index] = \
#             message[right_index], message[left_index]
#         left_index  += 1
#         right_index -= 1

# def reverse_words(message):
#     """
#     Takes a message as a list of characters and reverses the order of the words in place
#     * Space separated
    
#     >>> reverse_words(['a', ' ', 'c', 'a', 't'])
#     ['c', 'a', 't', ' ', 'a']

#     >>> reverse_words(['c', 'a', 't'])
#     ['c', 'a', 't']

#     >>> reverse_words([])
#     []

#     """
#     # Use above fxn
#     reverse_characters(message, 0, len(message)-1)

#     # Un-scramble each word
#     # current word start index
#     index = 0

#     for i in range(len(message) + 1):
#         if i == len(message) or message[i] == ' ':
#             reverse_characters(message, index, i - 1)

#             index += 1


def merge_lists(l1, l2):
    """
    Not done!
    We have our lists of orders sorted numerically already, in lists. 
    Write a function to merge our lists of orders into one sorted list.

    # >>> merge_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19])
    # [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

    """

    out = [None] * (len(l1) + len(l2))

    print(l1, len(l1))
    print(l2, len(l2))
    print(out, len(out))


    i = 0
    idx1 = 0
    idx2 = 0

    while i < len(out):
        print(i)
        curr1 = l1[idx1]
        curr2 = l2[idx2]
        print(curr1, curr2)

        if i < len(out):

            if curr1 < curr2:

                out[i] = curr1
                print("Out", out)
                i += 1
                idx1 += 1

            else:

                out[i] = curr2
                print("Out", out)
                i += 1
                idx2 += 1       

    print(out)
    return out

def is_riffle(half1, half2, deck):
    """
    Write a RECURSIVE function that takes a deck and checks if it has been shuffled in a "riffle" way

    ## If deck is a "riffle" of half1 and half2, the first card from deck
    ## should be either the same as the first card from half1 or the same as the 
    ## first card from half 2.

    ## Go through the deck, matching and throwing out as you match
    ## If we get to the end, return True

    Note this version is bad! Better version keeps track of indexes...


    """
    if len(deck) == 0:
        return True # Base case

    # If it exists, is the top of deck the same as the the top of half1?
    if len(half1) and half1[0] == deck[0]:
        # Take the tops off both and recurse
        return is_riffle(half[1:], half2[1:], deck[1:])

    # If it doesn't match, we know it's not:
    else:
        return False



def is_riffle_iter(half1, half2, deck, deck_ix=0, half1_ix=0, half2_ix=0):
    """
    Write a Better iterative RECURSIVE function that takes a deck and 
    checks if it has been shuffled in a "riffle" way

    Note this has better time complexity than the previous recursive version! 
    Instead of slicing the list, it just keeps track of indexes.

    """
    # base case is still the same, we have hit the end
    if deck_ix == len(deck):
        return True

    # If we still have cards in half1 and the top card is the same
    # as the top card in deck,
    if half1_ix < len(half1) and half1[half1_ix] == deck[deck_ix]:
        half1_ix += 1


    # If we still have cards in half2 and the top card is the same
    # as the top card in deck,
    elif half2_ix < len(half2) and half2[half2_ix] == deck[deck_ix]:
        half2_ix += 1

    # If either half is depleted OR there are not matches,
    else:
        return False

    #Move on to the next card:
    deck_ix += 1

    return is_riffle_iter(half1, half2, deck, deck_ix, half1_ix, half2_ix)


def is_riffle_best(half1, half2, deck):
    half1_ix = 0
    half2_ix = 0
    half1_max_ix = len(half1) - 1
    half2_max_ix = len(half2) - 1

    for card in deck:
        # If we still have cards in half1 and the "top" card in half1 is the same,
        if half1_ix <= half1_max_ix and card == half1[half1_ix]:
            half1_ix += 1

        # If we still have cards in half1 and the "top" card in half1 is the same,
        elif half2_ix <= half2_max_ix and card == half2[half2_ix]:
            half2_ix += 1

        else:
            return False

    # If all cards in shuffled deck have been accounted for, this is a riffle!
    return True


def time_equal(flight_length, movie_lengths):
    """Write a function that takes an integer flight_length (in minutes) and a
    list of integers movie_lengths (in minutes) and returns a
    boolean indicating whether there are two numbers in movie_lengths whose
    sum equals flight_length.

    >>> time_equal(0, [3, 3, 4])
    False
    >>> time_equal(10, [3, 7, 4])
    True
    >>> time_equal(100, [30, 70])
    True
    >>> time_equal(100, [])
    False

    Time is O(n) 

    Are you sure your function won’t give a false positive if the 
    list has one element that is half flight_length? 
    >> Solution : Pop the item once you get it

    """

    while len(movie_lengths) > 1:

        # Get the first item of movie_lengths:
        m1 = movie_lengths[0]

        # Create a set with the remaining elements:
        others = set(movie_lengths[1:]) # Oo this slice is bad, takes O(n)?

        # Get the value we are looking for:
        delta = flight_length - m1
        
        return delta in others # This takes O(n)

    return False


def perm_palin(string):
    """
    Write an efficient function that checks whether 
    any permutation ↴ of an input string is a palindrome. ↴

    >>> perm_palin("civic")
    True
    >>> perm_palin("ivicc")
    True
    >>> perm_palin("civil")
    False
    >>> perm_palin("livci")
    False

    HINT:
    - Check that each character left of the middle has a corresponding 
    copy right of the middle
    - Then check each character appears an even number of times
    - ONE char appears an odd number of times!
    - Data structure to use: DICTIONARY (with the char : boolean )

    # Overall time is O(n) + O(n) so still linear

    """

    # Create dict for characts:bools
    dic = {}

    # Iterate and add to dict: O(n)
    for char in string:
        parity = True # Stand in for Even Parity

        if string.count(char) % 2 == 1:
            parity = False # Stand in for Odd Parity

        dic[char] = parity


    # see if count of odd parity != 1 or 0 ... O(m)
    odd_count = [v for v in dic.values()].count(False)
    return odd_count == 1 or odd_count == 0


def has_pal_perm(string):
    # Their implementation. Faster?
    unpaired = {} # All unpaired characters

    for char in string:

        if char in unpaired:
            unpaired.remove(char)

        else:
            unpaired.add(char)

    return len(unpaired) <= 1



def word_cloud(string):
    """
    Build a word cloud, an infographic where the size of a word corresponds 
    to how often it appears in the body of text.
    Return a word count dictionary.
    
    >>> word_cloud("cloudy cloudy day")
    {'cloudy': 2, 'day': 1}

    >>> word_cloud("cloudy cloudy day day day")
    {'cloudy': 2, 'day': 3}

    >>> word_cloud("Cloudy cloudy Day day day")
    {'cloudy': 2, 'day': 3}

    >>> word_cloud("")
    {}

    """ 
    counts = {}
    listo = string.split(" ")

    # This method returns the value for the given key, if present in the 
    # dictionary. If not, then it will return None (if get() is used with 
    # only one argument).

    if len(listo) > 1:

        for item in listo:

            counts[item] = counts.get(item, 0) + 1


    return counts
















































# Doctest Section:
if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')

