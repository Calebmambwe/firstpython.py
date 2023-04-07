
# class Node(object):
#     def __init__(self,val=0, next=None):
#         self.val = val
#         self.next = next


# class Soluiton(object):
#     def merge_two_list(self, l1, l2):
#         if l1 is None:
#             return l2
#         elif l2 is None:
#             return l1
#         elif l1.val < l2.val:
#             l1.next = self.merge_two_list(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.merge_two_list(l2.next, l1)
#             return l2
#

#
# lst = Node("This")
# lst2 = Node("is ")
# lst3 = Node("it ")
#



class Node:
    def __init__(self, data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev



class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

            self.count += 1

    append("This")




