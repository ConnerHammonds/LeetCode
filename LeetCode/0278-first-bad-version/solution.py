# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        #n = 20, l = 0, m = 10      bad = 3
        #n = 9, l = 0, m = 4
        #n = 3, l = 0, m = 1
        #n = 3, l = 2, m = 2
        #n = 3, l = 3, m = 2

        while l <= n:
            m = (l + n) // 2
            if isBadVersion(m) == True:
                n = m - 1
            else:
                l = m + 1

        return l
        
