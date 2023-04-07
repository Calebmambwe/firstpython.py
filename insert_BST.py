class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.right = insert(root.left, key)
    return root


node = Node(9)
n1 = Node(7)
n2 = Node(3)
n3 = Node(1)
n4 = Node(10)
