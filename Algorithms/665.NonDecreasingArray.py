class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def check(nums):
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
            return True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if check(nums[:i] + nums[i+1:]):
                    return True
                if check(nums[:i+1] + nums[i+2:]):
                    return True
                return False
        return True
