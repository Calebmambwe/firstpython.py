
# not yet working
# def lengthOfLongestSubstring(s):
#     count = 0
#     count2 = 0
#     for i in range(len(s)):
#         a = s[i]
#         b = s[i + 1]
#         a.islower()
#         a.islower()
#         if ord(a) < ord(b):
#             count += 1
#         else:
#             count += 1
#             count2 = max(count2, count)
#
#     return count2


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         count = 0
#         j = 0
#         i = 0
#         max_ = 0
#         count = 0
#         seen = set()
#         while i < len(s):
#             # b = s[i - j + 1]
#             if s[i] in seen:
#                 seen.remove(s[i])
#                 j = i
#             else:
#                 seen.add(s[i])
#                 count += 1
#                 set_ = len(seen)
#                 max_ = max(max_, set_)
#             i += 1
#         return max_

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        j = 1
        i = 0
        max_ = 0
        count = 0
        seen = set()
        while i < len(s):
            # b = s[i - j + 1]

            if ord(s[i]) < ord(s[j]):
                seen.remove(s[i])
                j = i
            else:
                seen.add(s[i])
                count += 1
                set_ = len(seen)
                max_ = max(max_, set_)
            i += 1
        return max_

working
def lengthOfLongestSubstring(s):
    j = 1
    i = 0
    max_ = 0
    while j < len(s):
        a = s[i]
        b = s[i]
        a.islower()
        b.islower()
        if ord(a) < ord(b):
            i += 1
        elif a == b:
            j = 1
            i += 1
        else:
            j = i - j + 1
            i += 1
        max_ = max(max_, j)

    return i


lengthOfLongestSubstring("bbbbb")