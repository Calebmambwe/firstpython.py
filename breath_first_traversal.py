from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def breadth_first_values(root):
  if not root:
    return []

  queue = deque([ root ])
  values = []
  while queue:
    node = queue.popleft()
    values.append(node.val)

    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return values