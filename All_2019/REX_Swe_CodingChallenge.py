# Contents: three questions
# Timing: We recommend a 1.5 hour maximum. You are not required
# to finish each question. If you don't finish, please include 
# pseudocode or key ideas of your proposed solution.
#
# You are allowed to use outside resources if you wish


# 1. (Arrays) 
#    Write a function that swaps the first and last m elements
#    of an array, pairwise (That is, arr[0] swaps with arr[n-1],
#    arr[1] swaps with arr[n-2] and so on). Equivalently, the function
#    trades the first n elements with the last n elements and
#    reverses the order of both.
#
# Example input:
#    switch_ends([1, 2, 3, 14, 25, 26, 17, 8, 9, 10], 3)
# Example output:
#          [10, 9, 8, 14, 25, 26, 17, 3, 2, 1]
#
# Example input:
#    switch_ends([1, 2, 3, 14, 25, 26, 17, 8, 9, 10], 4)
# Example output:
#          [10, 9, 8, 17, 25, 26, 14, 3, 2, 1]


# your code here

def switch_ends(arr, n):
    """
    >>> switch_ends([1, 2, 3, 14, 25, 26, 17, 8, 9, 10], 3)
    [10, 9, 8, 14, 25, 26, 17, 3, 2, 1]
    >>> switch_ends([1, 2, 3, 14, 25, 26, 17, 8, 9, 10], 4)
    [10, 9, 8, 17, 25, 26, 14, 3, 2, 1]
    >>> switch_ends([26, 17, 8, 9, 10], 0)
    [26, 17, 8, 9, 10]
    >>> switch_ends([26, 17, 8, 9, 10], -1)
    [26, 17, 8, 9, 10]
    >>> switch_ends([], -1)
    []
    >>> switch_ends([1], 11)
    [1]
    """
    if n <= len(arr):
        for i in range(n):
            temp = arr[len(arr) - 1 - i]
            arr[len(arr) - 1 - i] = arr[i]
            arr[i] = temp
        
    return arr
    
# 2. (Strings and Trees)
#    Use OS.walk to pretty-print the directory structure of the server
#    That is, indent each folder name by its depth in the tree
#    and indent any contents of that folder one level more. Folder names 
#    should begin with /, and file names should not.
#
#    The particular order of the files and folders is not important
#    as long as the structure is accurate
#
#    Example output:
#    /home/coderpad
#        .profile
#        .bash_logout
#        README_IF_YOU_ARE_HACKING_ME
#        .bashrc
#        solution.py
#        ipython_config.py
#        pytest.ini
#        /.ipython
#            /nbextensions
#            /profile_default
#                history.sqlite
#                /log
#                /startup
#                    README
#                /db
#                /pid
#                /security
#            /extensions


# STARTER CODE
# Hey I used this: https://gist.github.com/kmanalo/8103281
# My final solution prints to console (does not return, I hope that's within the specs) and the order of the files is not correct. - Liv
import os
import pprint

def print_tree():
    pp = pprint.PrettyPrinter(indent=4)
    print(os.getcwd())
    
    for cur_path, folder_names, file_names in os.walk(os.getcwd()):
        
        # print('file_names', file_names)
        
        l = cur_path.replace(os.getcwd(), '').count(os.sep)
        # print('cur_path', cur_path)
        for fol in folder_names:
            print('{}/{}'.format(' '*4*(l + 1), os.path.basename(fol)))
            
            
            # for f in os.listdir(cur_path):
            #     if os.path.isfile(os.path.join(os.getcwd(), f)):
            #         print(f)
            # if files != []:
            #     for file in files:
            #         print('{}{}'.format(' '*4*(l + 1), os.path.basename(file)))
            
        for file in file_names:
            print('{}{}'.format(' '*4*(l + 1), os.path.basename(file)))
        
        
        

        

# 3. (Sorting/Data Structures)
#     Given an array of integers, write a function that does 2 things:
#      1. moves the non-zero elements to the left of the array (i.e. the front)
#      2. returns the array and the number of non-zero elements in the array
#     sample input: [1, 0, -5, 2, 0, 0, 7, 0, 0, 0]
#     sample result: [1, 2, -5, 7, 0, 0, 0, 0, 0, 0], 4
# your code here

def mv(arr):
    """
    # Hey I had to add parentheses to the test cases to make them pass
    # The first one is not in order, but the instructions don't seem to have any ordering (matching original or otherwise) so I left it the way it ran for me
    # - Liv
    
    >>> mv([1, 0, -5, 2, 0, 0, 7, 0, 0, 0])
    ([1, 2, -5, 7, 0, 0, 0, 0, 0, 0], 4)
    >>> mv([1, 5, 2, 0, 0, 7, 0])
    ([1, 5, 2, 7, 0, 0, 0], 4)
    >>> mv([])
    ([], 0)
    >>> mv([3, -3, 3])
    ([3, -3, 3], 3)
    """
    nz = [i for i in arr if i != 0]
    nz.extend([i for i in arr if i == 0])
    return nz, len(nz) - nz.count(0)
    



if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    print_tree()