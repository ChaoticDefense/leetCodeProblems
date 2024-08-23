# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n
        
        while L < R:
            M = L + ((R-L) // 2)
            if isBadVersion(M): # type: ignore
                R = M
            else:
                L = M + 1

        return L