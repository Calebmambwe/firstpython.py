import ctypes
class Node(object):
    def __init__(self, val):
        self.val = val
        self.both = 0


class XOR_linked_list(object):
    def __init__(self):
        self.head = self.tail = None
        self.__node = [] #This is to prevent gabage collection


    def add(self,node):
        if self.node is None:
            self.head = self.tail = node
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node

        self.__nodes.append(node)


    def get(self, index):
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.both

            if next_id:
                prev_id = id(node)
                node = self._get_obj(next_id)
            else:
                raise IndexError('Linked list index out of range')
        return node

    def _get_obj(id):
        return ctypes.cast(id, ctypes.py_object).value


LL = XOR_linked_list()
LL.head = Node(4)

print(LL.head.val)
