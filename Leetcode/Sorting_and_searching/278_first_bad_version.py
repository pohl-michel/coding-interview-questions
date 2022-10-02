# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j = 1, n
        while i <= j:
            if i == j:
                return i # because we know that there is a bad version
            mid = (i+j)//2
            if isBadVersion(mid):
                j = mid # it can be the first bad version
            else:
                i = mid+1 # the first bad version is strictly after i

    # better and more generic version:
    def firstBadVersion_v2(self, n: int) -> int:
        i, j = 1, n
        while i < j:
            mid = (i+j)//2
            if isBadVersion(mid):
                j = mid # it can be the first bad version
            else:
                i = mid+1 # the first bad version is strictly after i
        return i

    # - if we always have isBadVersion(mid) == True, then j always strictly decreases until i==j, and finally the program returns i
    # - if we always have isBadVersion(mid) == False, then i always increases by 1 until i==j and finally the program returns i