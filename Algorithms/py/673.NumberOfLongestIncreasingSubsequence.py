class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length_list = [1] * len(nums)
        count_list = [1] * len(nums)
        for i in range(len(nums)):
            smaller = [(length_list[j], j) for j in range(0, i) if nums[j] < nums[i]]
            if len(smaller) == 0:
                continue
            m = max(x[0] for x in smaller)
            length_list[i] = m + 1
            count_list[i] = sum(count_list[x[1]] for x in smaller if x[0] == m)
        m = max(length_list)
        s = 0
        for i in range(len(nums)):
            if length_list[i] == m:
                s += count_list[i]
        return s
