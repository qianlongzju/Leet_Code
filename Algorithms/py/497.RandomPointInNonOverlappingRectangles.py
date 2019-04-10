class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects

    def pick(self):
        """
        :rtype: List[int]
        """
        import random
        sum_area = 0
        for rect in self.rects:
            area = (rect[3] - rect[1] + 1) * (rect[2] - rect[0] + 1)
            sum_area += area
            if random.randint(1, sum_area) <= area:
                r = rect
        return random.randint(r[0], r[2]), random.randint(r[1], r[3])


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
