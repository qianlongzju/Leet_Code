class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        low, high = 0, nums[-1]-nums[0]
        while low < high:
            mid = low + ((high - low) // 2)
            j, count = 0, 0
            for i in range(1, n):
                while nums[i]-nums[j] > mid:
                    j += 1
                count += i-j
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low
