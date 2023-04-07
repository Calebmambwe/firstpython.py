def searchInsert(nums, target):
    res = []
    res.insert(0,"3")
    if target>nums[-1]:
            return len(nums)
    for i in enumerate(nums):
        if i[1]==target:
            return i[0]
        if i[1]>target:
            return i[0]

def searchInsert(nums, target):
    if target > nums[-1]:
        return len(nums)
    for idx, val in enumerate(nums):
        if val == target:
            return idx
        if val > target:
            return idx

searchInsert([1,3,5,6], 2)