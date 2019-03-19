class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        count = sorted(collections.Counter(nums).items())
        max_length = 0
        for i in range(1, len(count)):
            if count[i][0] == count[i-1][0] + 1:
                max_length = max(max_length, count[i][1] + count[i-1][1])
        return max_length
