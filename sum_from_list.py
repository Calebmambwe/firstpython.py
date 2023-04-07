#Brute Force approach O(n^2)
# def two_sum(lst, k):
#     for i in enumerate(lst):
#         for j in enumerate(lst):
#             if i != j and lst[i] + lst[j] == k:
#                 return True
#     return False
#
#
# two_sum([10, 15, 3, 7], 17)

#Using a set O(n)
# def two_sum(lst, k):
#     seen = set()
#
#     for num in lst:
#         if k - num in seen:
#            return True
#         seen.add(num)
#     return False
#
# two_sum([10, 15, 3, 7], 17)


from bisect import bisect_left
#Using Binary search
def two_sum(lst, k):
    lst.sort()

    for i in range(len(lst)):
        target = k - lst[i]
        j = binary_search(lst, target)

        if j == -1:
            continue
        elif j != i:
            return True
        elif j + 1 < len(lst) and lst[i + 1] == target:
            return True
        elif j - 1 >= 0 and lst[j - 1] == target:
            return True
    return False

def binary_search(lst, target):
    lo = 0
    hi = len(lst)
    ind = bisect_left(lst, target, lo, hi)

    if 0 <= ind < hi and lst[ind] == target:
        return ind
    return -1


two_sum([10, 15, 3, 7], 17)









