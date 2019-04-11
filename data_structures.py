""" 
data structures review:
- Binary Trees
- Maps 
- Linked Lists

"""

## BinaryTree():
    """
    Tree:
        nodes separated by edges
        a nonlinear data structure
        - first node is Root node
        - Every other node is associated with one parent node
        - Each node can have 0 or more child nodes

"""

class Node:
    """
    Node:
        - a concept that carries on for Tree, LList, and Map
        - for Tree, has self.left, self.right, and self.data
    """

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def __repr__(self):
        print(self.data)


class BinaryTree:

    def __init__(self, data):

