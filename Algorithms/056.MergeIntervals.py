# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        # TODO
        # the following is wrong
        #intervals = sorted(intervals)
        result = []
        v = intervals[0]
        i = 1
        while i < len(intervals):
            if v.end >= intervals[i].start:
                if intervals[i].end > v.end:
                    v.end = intervals[i].end;
            else:
                result.append(v)
                v = intervals[i]
            i += 1
        result.append(v)
        return result

if __name__ == '__main__':
    intervals = [Interval(1, 4), Interval(5, 6)]
    s = Solution()
    for r in s.merge(intervals):
        print "[%s, %s]" % (r.start, r.end), 
