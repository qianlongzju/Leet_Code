class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        # TODO
        # the following is wrong
        #intervals = sorted(intervals)
        result = []
        v = intervals[0]
        i = 1
        while i < len(intervals):
            if v[1] >= intervals[i][0]:
                if intervals[i][1] > v[1]:
                    v[1] = intervals[i][1];
            else:
                result.append(v)
                v = intervals[i]
            i += 1
        result.append(v)
        return result