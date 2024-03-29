# Write a function, linked_list_cycle, that takes in the head of a
# linked list as an argument. The function should return a boolean
# indicating whether or not the linked list contains a cycle.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_cycle(head):
    seen = set()
    current = head
    while current is not None:
        if current in seen:
            return True
        seen.add(current)
        current = current.next
    return False

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d
d.next = b # cycle

#         _______
#       /        \
# a -> b -> c -> d

linked_list_cycle(a)  # True