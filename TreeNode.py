class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class tree(object):
    def __init__(self, root):
        self.root = TreeNode(root)



treeno = tree(1)
treeno.root.left = TreeNode(2)