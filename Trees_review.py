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


class BinarySearchNode(object):
    """Binary Tree Node with two children / pointers """
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






