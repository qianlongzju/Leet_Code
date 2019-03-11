class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        flag = 1
        n = len(nums)
        if n > 10 and 2 * k > n:
            flag = -1
            k = n - k + 1
            nums = [-1 * i for i in nums]
        q = nums[:k]
        import heapq
        heapq.heapify(q)
        for i in range(k, len(nums)):
            if nums[i] > q[0]:
                heapq.heappop(q)
                heapq.heappush(q, nums[i])
        return flag * q[0]
