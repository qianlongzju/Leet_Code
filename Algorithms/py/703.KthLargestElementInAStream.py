class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        import heapq
        heapq.heapify(nums)
        self.k = k
        self.nums = nums
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k or val > self.nums[0]:
            heapq.heappush(self.nums, val)
            
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
