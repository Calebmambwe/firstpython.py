from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_include(root, target):
    if not root:
        return False

    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.val == target:
            return True

        if queue.left:
            queue.append(queue.left)
        if queue.right:
            queue.append(queue.right)
    return False


# recursive version

# def tree_includes(root, target):
#     if not root:
#         return False
#
#     if root.val == target:
#         return True
#
#     return tree_includes(root.left, target) or tree_includes(root.right, target)