# def moveZeroes(nums):
#     temp = None
#     for i, num in enumerate(nums):
#         if num == 0:
#           zero = nums[i]
#           nums.append(zero)
# def moveZeroes(nums):
#     pos = 0
#     for i in range(len(nums)):
#         el = nums[i]
#         if el != 0:
#             nums[pos], nums[i] = nums[i], nums[pos]
#             pos += 1

# def moveZeroes(nums):
#     for i, char in enumerate(nums):
#         if char == 0:
#             nums.append(nums.pop(i))

# class Solution(object):
#     def moveZeroes(self, nums):
#         i = count = 0
#         while count < len(nums):
#             if nums[i] == 0: nums.append(nums.pop(i))
#             else: i += 1
#             count += 1

# def moveZeroes(nums):
#     append_times=nums.count(0)
#     for i in range(append_times):
#         nums.remove(0) #  Delete the front zero
#         nums.append(0)

# def moveZeroes(nums):
#     i = count = 0
#     while count < len(nums):
#         if nums[i] == 0: nums.append(nums.pop(i))
#         else: i += 1
#         count += 1

moveZeroes([0, 0, 1])
