def first_missing_positive(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return print(i)


first_missing_positive([-2,-1,3,4,5])

