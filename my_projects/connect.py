class Solution:

    def connect(self, root):
        if not root:
            return None

        head = root
        node = (0, None)

        queue = []
        queue.append((root, 0))
        level = 0
        while queue:
            root, level = queue.pop(0)
            if node[0] > 0 and level == node[0]:
                node[1].next = root
            node = (level, root)

            if root.left:
                queue.append((root.left, level + 1))
            if root.right:
                queue.append((root.right, level + 1))

        return head


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node', n = None) -> 'Node':

        if not root: return
        root.next = n

        self.connect(root.left,root.right)
        self.connect(root.right, n.left if n else None)

        return root

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(node):
            if node.left:  # as if left child is there, so right is.
                if node.next:
                    node.right.next = node.next.left
                node.left.next=node.right
                dfs(node.right)
                dfs(node.left)
        if root:
            dfs(root)
        return root