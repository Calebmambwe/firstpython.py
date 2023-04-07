class listNode():
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def merge_two_list(self, l1, l2):
        if l1 is None:
            return  l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.merge_two_list(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_list(l2.next, l1)
            return l2


lst = [1,2,4]
lst2 = [5,6,7]

merge_two_list()


