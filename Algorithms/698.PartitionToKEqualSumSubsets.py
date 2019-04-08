class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        s = sum(nums)
        if s % k != 0:
            return False
        target = s / k
        subsets = [target] * k
        def helper(i):
            if i == len(nums):
                return True
            for j in range(k):
                if subsets[j]-nums[i] == 0 or (j < len(nums)-1 and subsets[j]-nums[i] >= nums[-1]):
                    subsets[j] -= nums[i]
                    if helper(i+1):
                        return True
                    subsets[j] += nums[i]
            return False
        return helper(0)
