def longest_substring(str_num):
    start = len(str_num) + 1
    end = len(str_num)-1
    i = 0

    while not end:
        if str_num[i] == start:
            len(str_num) + 1
    else:
        print(str_num[i])
        i += 1


# def longest_substring(str_num):
#     n = len(str_num)
#
#     res = 0
#     for i in range(n):
#         for j in range(i, n):
#             if check(i, j):
#                 res = max(res, j - i + 1)
#     return res
#

str_num = "abbssc"
longest_substring(str_num)

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         def check(start, end):
#             chars = [0] * 128
#             for i in range(start, end + 1):
#                 c = s[i]
#                 chars[ord(c)] += 1
#                 if chars[ord(c)] > 1:
#                     return False
#             return True
#
#         n = len(s)
#
#         res = 0
#         for i in range(n):
#             for j in range(i, n):
#                 if check(i, j):
#                     res = max(res, j - i + 1)
#         return res

# def length_of_substring(str):


# def longest_substring(str_num):
#     i = 0
#     j = 1
#
#     while i < len(str_num):
#         if str_num[i] == str_num[j]
#             j += 1
#         else:
#             print(str_num[i])
#             i += 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


print(Solution().lengthOfLongestSubstring("Callalsllsllllllssss"))

# str_num = "abbssc"
# longest_substring(str_num)
