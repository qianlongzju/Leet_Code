class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count, count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                flag = False
                max_count = max(max_count, count)
                count = 0
            else:
                flag = True
                count += 1
        else:
            max_count = max(max_count, count)
        return max_count
