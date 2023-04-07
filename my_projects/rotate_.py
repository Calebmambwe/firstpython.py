def rotate(self, nums: List[int], k: int) -> None:
    k %= len(nums)
    nums[k:], nums[:k] = nums[:-k], nums[-k:]


    # not in place
    # def rotate(nums, k):
    #     num_len = len(nums)
    #     result = []
    #     last = num_len - k
    #     while last:
    #         result.append(nums.pop())
    #         last -= 1
    #     return [*result, *nums]
    #
    # rotate([1, 2, 3, 4, 5, 6, 7], 3)

    from collections import deque

# not in place
    # class Solution:
    #     def rotate(self, nums: List[int], k: int) -> None:
    # # nums = deque(nums)
    # # nums_len = len(nums)
    # # i = 0
    # # while i < nums_len:
    # #     nums.append(nums.popleft())
    # #     nums_len -= 1
    # #     i += 1