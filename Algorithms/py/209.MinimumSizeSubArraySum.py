class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = None
        start = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total >= target:
                while start < i and total-nums[start] >= target:
                    total -= nums[start]
                    start += 1
                if min_length == None:
                    min_length = i - start + 1
                else:
                    min_length = min(min_length, i-start+1)
        if min_length == None:
            return 0
        else:
            return min_length