class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        s = sum(nums)
        d = set()
        for n in nums:
            if n in d:
                return [n, l*(l+1)/2 - s + n]
            d.add(n)
