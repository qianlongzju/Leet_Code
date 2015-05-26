class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        maximum, i = 0, 0
        while i < len(nums) and i <= maximum:
            maximum = max(i + nums[i], maximum)
            if maximum >= len(nums) - 1:
                return True
            i += 1
        return False
