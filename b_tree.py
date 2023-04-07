class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def serialize(self, root: Node) -> str:
    #     self.lst = []
    #     def dfs(node):
    #         if not node: return
    #         self.lst.append(node.vol)
    #         dfs(node.left)
    #         dfs(node.right)
    #     dfs(root)
    #     return "," .join(map, self.lst
    #
    #
    # def deserialize(self, data: str) -> Node:
    #     if not data: return None
    #     lst = [int(d) for d in data.split(",")]
    #
    #     def rec(lst, lower, upper):
    #         if not lst: return None
    #         if not lower <= upper: return None
    #
    #     cand = lst.pop(0)
    #     root = TreeNode(cand)
    #
    #     root.left = rec(lst, lower, root, val)
    #     root.right = rec(lst, root.val, upper)
    #
    #     return root
    # return rec(lst,-float('inf'),float('inf'))
    #
    #

def serialize(root):
    if root is None: return '#'
    return '{}{}{}'.format(root.val, serialize(root.left), serialize(root.right))


def deserialize(data):
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()

