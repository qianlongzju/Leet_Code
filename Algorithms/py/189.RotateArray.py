class Solution(object):
    def rotate_swap(self, nums, k):
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

    def rotate(self, nums, k):
        k %= len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

    def rotate_old(self, nums, k):
        k %= len(nums)
        self.reverse(nums)
        nums[:k] = self.reverse(nums[:k])
        print nums
        nums[k:] = self.reverse(nums[k:])

    def reverse(self, nums):
        i, j = 0, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j-1
        n = len(nums)
        k %= n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n -1)