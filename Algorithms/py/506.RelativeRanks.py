class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        l = [(num, i) for i, num in enumerate(nums)]
        l = sorted(l, reverse=True)
        n = len(l)
        result = [None] * n
        for i in range(n):
            if i == 0:
                result[l[i][1]] = "Gold Medal"
            elif i == 1:
                result[l[i][1]] = "Silver Medal"
            elif i == 2:
                result[l[i][1]] = "Bronze Medal"
            else:
                result[l[i][1]] = str(i+1)
        return result
