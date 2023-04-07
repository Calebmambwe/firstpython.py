class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class stack:
    def __init__(self, data= None):
        self.data = data
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1


