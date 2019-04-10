class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = nums[0], None, None
        for i in range(1, len(nums)):
            num = nums[i]
            if num > first:
                first, second, third = num, first, second
            elif num < first and (second == None or second < num):
                second, third = num, second
            elif num < second and (third == None or third < num):
                third = num
        return third if third != None else first
