class CountIntervals(object):

    def __init__(self):
        self.intervals = []

    def add(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        tmp = []
        for i, interval in self.intervals:
            l, r = interval
            if l > right:
                break
            if l <= left <= r and l <= right <= r:
                return
            if left <= l <= right and left <= r <= right:
                tmp.append(i)
            if l <= left <= r:
                tmp.append(i)

    def count(self):
        """
        :rtype: int
        """
        res = 0
        for l, r in self.intervals:
            res += r - l + 1
        return res


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
