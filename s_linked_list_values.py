class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
  values = []
  current = head
  while current is not None:
     
    current = current.next
  return print(values)

#recursive

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
#
# def linked_list_values(head):
#   values = []
#   fill_values(head,values)
#   return values
#
# def fill_values(head,values):
#   if values is None:
#     return
#   values.append(head.val)
#   fill_values(head,values)
#

  # driver
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

linked_list_values(a)