# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals == []:
            return 0
        intervals.sort(key=lambda x:(x.end, x.start))
        #intervals = sorted(intervals, key=lambda x:(x.start, x.end))
        count = 1
        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur.start >= prev.end:
                prev = cur
                count += 1
        return len(intervals) - count
