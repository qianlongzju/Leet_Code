class Solution:
    # @param nums, a list of integer
    # @return an integer
    def findMin(self, nums):
        start, end = 0, len(nums)-1
        while start < end and nums[start] >= nums[end]:
            mid = start + (end - start)/2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                start += 1
        return nums[start]
    #def findMin(self, nums):
    #    return self.findMin_interval(nums, 0, len(nums)-1)

    #def findMin_interval(self, nums, start, end):
    #    if start == end:
    #        return nums[start]
    #    if nums[start] < nums[end]:
    #        return nums[start]
    #    mid = start + (end - start) / 2
    #    if nums[start] == nums[end]:
    #        return self.findMin_interval(nums, start+1, end)
    #    if nums[mid] >= nums[start]:
    #        return self.findMin_interval(nums, mid+1, end)
    #    return self.findMin_interval(nums, start, mid)
