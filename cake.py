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

def reverse_characters(message, left_index, right_index):
    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index  += 1
        right_index -= 1

def reverse_words(message):
    """
    Takes a message as a list of characters and reverses the order of the words in place
    * Space separated
    
    >>> reverse_words(['a', ' ', 'c', 'a', 't'])
    ['c', 'a', 't', ' ', 'a']

    >>> reverse_words(['c', 'a', 't'])
    ['c', 'a', 't']

    >>> reverse_words([])
    []

    """
    # Use above fxn
    reverse_characters(message, 0, len(message)-1)

    # Un-scramble each word
    # current word start index
    index = 0

    for i in range(len(lst) + 1):
        if i == len(message) or message[i] == ' ':
            reverse_characters(message, index, i - 1)

            index += 1




# Doctest Section:
if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')

