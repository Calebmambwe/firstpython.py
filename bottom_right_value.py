from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bottom_right_value(root):
    if root is None:
        return None

    queue = deque([root])
    while queue:
        current = queue.popleft()

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return current.val