class Solution:
    def removeDuplicates(self, A):
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                j += 1
                nums[j] = nums[i]
        return j+1
