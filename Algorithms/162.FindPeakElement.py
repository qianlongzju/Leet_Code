class Solution:
    # @param nums, a list of integer
    # @return an integer
    def findPeakElement(self, nums):
        return self.findPeakElementInterval(nums, 0, len(nums)-1)

    def findPeakElementInterval(self, nums, start, end):
        if start == end:
            return start
        mid = start + (end - start)/2
        if (mid == 0 or nums[mid] > nums[mid-1]) and (mid+1 > end or nums[mid] > nums[mid+1]):
            return mid
        elif (mid == 0 or nums[mid] > nums[mid-1]) and (mid+1 > end or nums[mid] < nums[mid+1]):
            return self.findPeakElementInterval(nums, mid+1, end)
        else:
            return self.findPeakElementInterval(nums, start, end-1)
