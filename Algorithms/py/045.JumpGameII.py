class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        maximum, i, steps = 0, 0, [None for j in range(len(nums))]
        steps[0] = 0
        while i < len(nums) and i <= maximum:
            for j in range(maximum+1, min(i+nums[i]+1, len(nums))):
                if not steps[j]:
                    steps[j] = steps[i] + 1
            maximum = max(i + nums[i], maximum)
            if maximum >= len(nums)-1:
                return steps[-1]
            i += 1

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        steps = [n-1]*n
        steps[0] = 0
        for i in range(n):
            for j in range(i+1, min(i+nums[i]+1, n)):
                steps[j] = min(steps[j], steps[i] + 1)
        #print(steps)
        return steps[-1]
