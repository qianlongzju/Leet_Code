class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums = sorted(nums)
        if sum(nums[0:4]) > target or sum(nums[-4:]) < target:
            return []
        result = set()
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                k = j + 1
                l = n - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total < target:
                        k += 1
                    elif total > target:
                        l -= 1
                    else:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                j += 1
            i += 1
        return [list(a) for a in result]
