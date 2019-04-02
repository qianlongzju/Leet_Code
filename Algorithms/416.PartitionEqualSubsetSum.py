class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s / 2
        print(target)
        def helper(i, target):
            if i == len(nums):
                return False
            if target == nums[i]:
                return True
            if target-nums[i] < nums[-1]:
                return False
            target -= nums[i]
            for j in range(i+1, len(nums)):
                if helper(j, target): 
                    return True
            return False
        for i in range(len(nums)):
            if nums[i] > target:
                return False
            if helper(i, target):
                return True
        return False
