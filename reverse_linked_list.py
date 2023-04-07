class Node:
    def __init__(self, val =None):
        self.val = val
        self.next = None


def reverse(head_of_list):
    current_node = head_of_list
    previous_node = None
    next_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node

        previous_node = current_node
        current_node = next_node

    return previous_node


r1 = Node(1)
r2 = Node(2)
r3 = Node(3)
r4 = Node(4)
r5 = Node(5)

r1.next = r2
r2.next = r3
r3.next = r4
r4.next = r5



reverse(r1)
