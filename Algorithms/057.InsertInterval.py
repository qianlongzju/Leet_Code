class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        i = 0
        while i < len(intervals):
            if newInterval.start > intervals[i].end:
                result.append(intervals[i])
            elif newInterval.end < intervals[i].start:
                break
            else:
                if newInterval.end < intervals[i].end:
                    newInterval.end = intervals[i].end
                if newInterval.start > intervals[i].start:
                    newInterval.start = intervals[i].start
            i += 1
        result.append(newInterval);
        result.extend(intervals[i:])
        return result
