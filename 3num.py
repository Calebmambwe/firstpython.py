# class solution:
#     def threesum(self, nums):
#         result = []
#         for i1 in range(0, len(nums)):
#             for i2 in range(i1+1, len(nums)):
#                 for i3 in range(i2+1, len(nums)):
#                     a, b, c = nums[i1], nums[i2], nums[i3]
#                     if a + b + c == 0:
#                         result.append([a, b, c])
#         return result
#
    # def threesumindices(self, nums):
    #     nums.sort()
    #     result = []
    #     for i in range(len(nums)):
    #         self.twosumindices(nums, i, result)
    #     return result
    #
    # def twosumindices(self, nums, start, result):
    #     low = start + 1
    #     high = len(nums)-1
    #     while low < high:
    #         sum = nums[start] + nums[low] + nums[high]
    #         if sum == 0:
    #             result.append([nums[start], nums[low], nums[high]])
    #             low += 1
    #             high -= 1
    #         elif sum < 0:
    #             low += 1
    #         else:
    #             high -= 1
    #     return result


# print(solution().threesum([-1,0,1,2,-4,-3]))
# print(solution().threesumindices([-1, 0, 1, 2, -1, -4]))

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
