class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums);
        self.swap(nums, 0, len(nums)-1);
        self.swap(nums, 0, k-1);
        self.swap(nums, k, len(nums)-1)
                
    def swap(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
