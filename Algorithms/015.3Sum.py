class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, nums):
        result = set()
        nums = sorted(nums)
        n = len(nums)
        i = 0
        while i < n:
            while i > 0 and i < n and nums[i] == nums[i-1]:
                i += 1
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif total > 0:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
            i += 1
        return [list(a) for a in result]
