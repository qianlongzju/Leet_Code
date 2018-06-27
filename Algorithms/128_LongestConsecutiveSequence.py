class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = set(nums)
        longestLength = 0
        for i in nums:
            length = 1
            j = i+1
            while j in m:
                m.remove(j)
                j += 1
                length += 1
            j = i-1
            while j in m:
                m.remove(j)
                j -= 1
                length += 1
            longestLength = max(longestLength, length)
        return longestLength
