# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def get_node_value(head, index):
#     if head is None:
#         return None
#
#     if index == 0:
#         return head.val
#
#     return get_node_value(head.next, index - 1)

#iteratively

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index):
    current = head
    count = 0
    while current is not None:
        if index == count:
            return current.val
        current = current.next
        count += 1

    return None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 2) # 'c'