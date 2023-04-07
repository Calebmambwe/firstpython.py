# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def sum_list(head):
#   if head is None:
#     return 0
#   return head.val + sum_list(head.next)

#iteratively
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_list(head):
    current = head
    total_sum = 0
    while current is not None:
        total_sum += current.val
        current = current.next
    return print(total_sum)

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

sum_list(a)
