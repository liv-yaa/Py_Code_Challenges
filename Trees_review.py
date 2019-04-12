"""Tree class and tree node class.

Binary Search Node too

Copied from lecture (Trees I) demo!


"""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node {data}>".format(data=self.data)

    def find(self, data):
        """
        A "depth first search" meaning,  we are going to search all children of the
        durrent node before going on to the next sibling. 


        Return node object with this data.
        
        Start here. Return None if not found.
        
        https://fellowship.hackbrightacademy.com/materials/ft25a/lectures/trees/
        """

        # Initialize a list of all nodes to_visit. This is a STACK!!! ***z        
        to_visit = [self]

        while to_visit:
            current = to_visit.pop() # In any case, remove current from to_visit

            if current.data == data: # If we have found data, return current=data
                return current

            #else, if we have not found data, add all the children of current to to_visit!
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



class BidirectionalNode(object):
    """Node that is bidirectional.
    Used to make a "doubly linked tree"
    Useful in "relational" databases

    """

    def __init__(self,
                 parent,
                 children):
        self.parent = parent
        self.children = children



class BinarySearchNode(object):
    """Binary Tree Node with two children / pointers 
    Also a tree, made of nodes
    But each node has a left and right child
    Has a “rule” for arrangement
    Often used for fast searching


    Reviewing this in order to do this LeetCode problem:
            
        Combine these two trees. If they positionally overlap, SUM the values
        to create the new node.

        Otherwise, the None node will be used as the node of the new tree.

        Input: 
            Tree 1                     Tree 2                  
                  1                         2                             
                 / \                       / \                            
                3   2                     1   3                        
               /                           \   \                      
              5                             4   7                  
        Output: 
        Merged tree:
                 3
                / \
               4   5
              / \   \ 
             5   4   7
             
         Note: The merging process must start from the root nodes of both trees.

        I'm thinking depth-first adding to tree
        The order of input is a bredth-first search




    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode {data}>".format(data=self.data)

    def find(self, sought):
        """
        Return node with this data. 
        **Fast searching algorithm -- every choice we make reduces options by half O(log n)
                                        (if balanced properly)
        **

        Start here and return None if not found.

        """
        current = self

        while current:

            print("checking", current.data)

            if current.data == sought:
                return current

            elif sought < current.data:
                current = current.left

            elif sought > current.data:
                current = current.right

    def traverse_in_order(self):
        """ Traverse a binary subtree in order
            - Left, Parent, Right
            From left to right, pretty much
            Uses: 
            - Returning the nodes from a binary search tree in order "Left first" :)
        """

        def recurse_in_order(node):
            if node:
                recurse_in_order(node.left)
                print(node.data)
                recurse_in_order(node.right)
            # Else if it doesn't have data, is it None?

        recurse_in_order(self)

    def traverse_pre_order(self):
        """ Traverse a binary subtree in pre-order
            - Parent, Left, Right
            - "Depth first Left" so add all the leftmost people until left = None, then add Right, then go up to root's sibling.
            - Useful for duplicating Binary Trees & parsing math "expression tress"
        
        """

        def recurse_pre_order(node):
            if node:
                print(node.data)
                recurse_pre_order(node.left)
                recurse_pre_order(node.right)
            # Else if it doesn't have data, is it None?

        recurse_pre_order(self)


    def traverse_post_order(self):
        """ Traverse a binary subtree in post-order
            - Parent, Left, Right
            - "Depth first Left" so add all the leftmost people until left = None, then add Right, then go up to root's sibling.
            - Useful for duplicating Binary Trees & parsing math "expression tress"
            - Useful for deleting a Binary Tree
        
        """

        def recurse_post_order(node):
            if node:
                recurse_post_order(node.left)
                recurse_post_order(node.right)
                print(node.data)
        recurse_post_order(self)













if __name__ == '__main__':
    # Make an example tree and search for things in it

    # resume = Node("resume.txt", [])
    # recipes = Node("recipes.txt", [])
    # jane = Node("jane/", [resume, recipes])
    # server = Node("server.py", [])
    # jessica = Node("jessica/", [server])
    # users = Node("Users/", [jane, jessica])
    # root = Node("/", [users])

    # tree = Tree(root)
    # print("server.py = ", tree.find_in_tree("server.py"))  # should find
    # print("style.css = ", tree.find_in_tree("style.css"))  # should not find

    # Make an example BinarySearchTree and search for nodes in it

    apple = BinarySearchNode("apple")
    ghost = BinarySearchNode("ghost")
    fence = BinarySearchNode("fence", apple, ghost)
    just = BinarySearchNode("just")
    jackal = BinarySearchNode("jackal", fence, just)
    zebra = BinarySearchNode("zebra")
    pencil = BinarySearchNode("pencil", None, zebra)
    mystic = BinarySearchNode("mystic")
    nerd = BinarySearchNode("nerd", mystic, pencil)
    money = BinarySearchNode("money", jackal, nerd)

    print("nerd = ", money.find("nerd"))     # should find
    print("banana = ", money.find("banana"))  # shouldn't find






