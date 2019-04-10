# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.mapping = {}
        return self.firstBadVersionRange(1, n)
    
    def firstBadVersionRange(self, start, end):
        mid = start + (end - start) / 2
        if isBadVersion(mid):
            if mid == 1:
                return mid
            if mid-1 in self.mapping:
                return mid
            self.mapping[mid] = True
            return self.firstBadVersionRange(start, mid-1)
        else:
            self.mapping[mid] = False
            if mid+1 in self.mapping and self.mapping[mid+1] == True:
                return mid+1
            return self.firstBadVersionRange(mid+1, end)
