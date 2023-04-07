# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#
# def create_linked_list(values):
#     dummy_node = Node(None)
#     tail = dummy_node
#     for val in values:
#         tail.next = Node(val)
#         tail = tail.next
#
#     return dummy_node.next


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(values, i = 0):
  if i == len(values):
    return None
  head = Node(values[i])
  head.next = create_linked_list(values, i + 1)
  return head