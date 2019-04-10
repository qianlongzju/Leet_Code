class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        sum_w = 0
        self.sum = [0] * len(w)
        for i, weight in enumerate(w):
            sum_w += weight
            self.sum[i] = sum_w

    def pickIndex(self):
        """
        :rtype: int
        """
        import random
        w = random.randint(1, self.sum[-1])
        left = 0
        right = len(self.sum) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.sum[mid] < w:
                left = mid + 1
            else:
                right = mid
        return right


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
