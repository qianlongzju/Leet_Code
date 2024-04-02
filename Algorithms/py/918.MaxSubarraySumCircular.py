class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxEndingHere, maxSoFar = nums[0], nums[0]
        minEndingHere, minSoFar = nums[0], nums[0]
        for i in range(1, len(nums)):
            maxEndingHere = max(nums[i], maxEndingHere + nums[i])
            maxSoFar = max(maxSoFar, maxEndingHere)

            minEndingHere = min(nums[i], minEndingHere + nums[i])
            minSoFar = min(minSoFar, minEndingHere)
        if maxSoFar <0:
            return maxSoFar
        return max(maxSoFar, sum(nums) - minSoFar)