class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        maximum = None
        for k, v in counter.items():
            if maximum == None or v > maximum:
                keys = [k]
                maximum = v
            elif v == maximum:
                keys.append(k)
        shortest = len(nums)
        for k in keys:
            for i in range(len(nums)):
                if nums[i] == k:
                    break
            for j in range(len(nums)-1, -1, -1):
                if nums[j] == k:
                    break
            shortest = min(shortest, j-i+1)
        return shortest
