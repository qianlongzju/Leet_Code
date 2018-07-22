class Solution:
    # @return an integer
    def threeSumClosest(self, nums, target):
        result = set()
        nums = sorted(nums)
        n = len(nums)
        i = 0
        closestSum = nums[0] + nums[1] + nums[2]
        min_gap = abs(closestSum - target)
        while i < n:
            while i > 0 and i < n and nums[i] == nums[i-1]:
                i += 1
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                gap = abs(total - target)
                if gap < min_gap:
                    closestSum = total
                    min_gap = gap
                if total < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif total > target:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    return closestSum
            i += 1
        return closestSum
