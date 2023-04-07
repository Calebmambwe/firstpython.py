class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
#
# def max_path_sum(root):
#     if root is None:
#         return float("-inf")
#
#     if root.left is None and root.right is None:
#         return root.val
#
#     max_left = max_path_sum(root.left)
#     max_rigth = max_path_sum(root.right)
#     return root.val + max_left + max_rigth
#
def max_path_sum(root):
    if root is None:
        return float("-inf")

    if root.left is None and root.right is None:
        return root.val

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))