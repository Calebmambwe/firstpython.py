def middleNode(head):
    result = []
    current = head
    while current is not None:
        if current.val not in result:
            result.append(current.val)
        current = current.next
    mid = len(result) // 2
    current = head
    while current is not None:
            if mid == 0:
                return current
            mid -= 1
            current = current.next


# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def middleNode(head):
#     arr = [head]
#     while arr[-1].next:
#         arr.append(arr[-1].next)
#     return arr[len(arr) // 2]

# def middleNode(head):
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow


# def middleNode(head):
#     depth = 1
#     nodes = {}
#     while head:
#         nodes[depth] = head.val
#         head = head.next
#         depth += 1
#
#     return nodes[(depth // 2) + 1] if depth % 2 else nodes[(depth // 2)]
