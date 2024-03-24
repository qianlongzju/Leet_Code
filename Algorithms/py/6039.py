class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heapq.heapify(nums)
        while k > 0:
            x = heapq.heappop(nums)
            x += 1
            k -= 1
            heapq.heappush(nums, x)
        #print(nums)
        result = nums[0]
        for i in range(1, len(nums)):
            result = (result * nums[i]) % (10**9 + 7)
        return result
