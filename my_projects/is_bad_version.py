class Solution:
    def firstBadVersion(self, n):
        for num in range(0,n):
            if isBadVersion(n) == False:
                return
        return num


