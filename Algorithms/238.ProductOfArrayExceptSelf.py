class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n
        for i in range(1, n):
            result[i] = nums[i-1] * result[i-1]
        tmp = 1
        for i in range(n-2, -1, -1):
            tmp *= nums[i+1]
            result[i] *= tmp
        return result
        
    def helper(self, nums):
        n = len(nums)
        left2right, right2left = [1] * n, [1] * n
        left2right[0], right2left[-1] = nums[0], nums[-1]
        for i in range(1, n):
            left2right[i] = left2right[i-1] * nums[i]
            right2left[-i - 1] = right2left[-i] * nums[-i-1]
        result = [1] * n
        for i in range(1, n-1):
            result[i] = left2right[i-1] * right2left[i+1]
        result[0], result[-1] = right2left[1], left2right[-2]
        return result
