# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# def depth_first_values(root):
#     if not root:
#         return []
#
#     stack = [root]
#     values = []
#     while stack:
#         node = stack.pop()
#         values.append(node.val)
#         if node.right:
#             stack.append(node.right)
#         if node.left:
#             stack.append(node.left)
#     return values

#recursive
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_first_values(root):
    if not root:
        return []

    left_values = depth_first_values(root.right)
    right_values = depth_first_values(root.left)

    return [root.val, *left_values, *right_values]
 