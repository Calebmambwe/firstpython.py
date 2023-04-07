# Not yetworking 
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         def twoSum(numbers, target):
#             seen = {}
#             sum = 0
#             for i in enumerate(numbers):
#                 sum = target - i[1]
#                 if sum in seen:
#                     return i[0], seen[sum]
#                 seen[i[1]] = i[0]