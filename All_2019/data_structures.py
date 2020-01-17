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
        pass



"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node {data}>".format(data=self.data)

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)



class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root={root}>".format(root=self.root)

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find(data)

