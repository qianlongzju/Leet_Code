class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 1, len(nums)-1
        while i <= j:
            mid = i + ((j - i) // 2)
            count = 0
            mid_count = 0
            for num in nums:
                if num < mid:
                    count += 1
                if num == mid:
                    mid_count += 1
                    if mid_count > 1:
                        return mid
            if count <= mid-1:
                i = mid + 1
            else:
                j = mid - 1
        return i
