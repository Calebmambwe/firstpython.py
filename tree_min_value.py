# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
#
# def tree_min_value(root):
#     if root is None:
#         return float("inf")
#
#     min_letf = tree_min_value(root)
#     min_rigth = tree_min_value(root)
#     return min(root.val, min_letf,min_rigth)

#DFS iteeratively

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_min_value(root):
    if root is None:
        return float("inf")

    smallest = float("inf")
    stack = [root]
    while stack:
        current = stack.pop()
        if current.val < smallest:
            smallest = current.val

        if current.left is not None:
            stack.append(current.val)
        if current.right is not None:
            stack.append(current.val)

    return smallest

