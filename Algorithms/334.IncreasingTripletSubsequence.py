class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = None
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                continue
            else:
                if t == None:
                    t = (nums[i-1], nums[i])
                elif t[-1] < nums[i]:
                    return True
                elif t[-2] < nums[i-1]:
                    return True
                else:
                    t = (nums[i-1], nums[i])
        return False
