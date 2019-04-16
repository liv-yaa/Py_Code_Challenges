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





# Doctest Section:
if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')

